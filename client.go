package main

import (
	pb "DH_FUL/pb"
	"context"
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
	"strconv"
	"time"

	"google.golang.org/grpc"
)

const (
	addr        = "localhost:50051"
	pub_key     = 197197
	private_key = 199199
)

func main() {
	conn, err := grpc.Dial(addr, grpc.WithInsecure(), grpc.WithBlock())

	if err != nil {
		log.Fatal(err)
	}

	defer conn.Close()

	c := pb.NewGreeterClient(conn)

	name := strconv.Itoa(pub_key)

	ctx, cancell := context.WithTimeout(context.Background(), time.Second)
	defer cancell()

	r, err := c.SayHello(ctx, &pb.MessageRequest{Name: name})
	if err != nil {
		log.Fatalf("Could not greet: %v", err)
	}

	log.Printf("Server's public key: %s", r.Message)
	fmt.Println(r.Message)
	curl2(r.Message)
}

func curl2(name2 string) {
	conn, err := grpc.Dial(addr, grpc.WithInsecure(), grpc.WithBlock())

	if err != nil {
		log.Fatal(err)
	}

	defer conn.Close()

	c := pb.NewGreeterClient(conn)
	name := name2
	//server_pub_key, _ := strconv.Atoi(name)
	part_key := generate_part_key(name)
	ctx, cancell := context.WithTimeout(context.Background(), time.Second)
	defer cancell()

	r, err := c.SayHello2(ctx, &pb.Message2Request{Name: part_key})
	if err != nil {
		log.Fatalf("Could not greet: %v", err)
	}

	log.Printf("Server's part key: %s", r.Message)
	curl3(r.Message)
}

func curl3(name3 string) {
	conn, err := grpc.Dial(addr, grpc.WithInsecure(), grpc.WithBlock())

	if err != nil {
		log.Fatal(err)
	}

	defer conn.Close()

	c := pb.NewGreeterClient(conn)
	name := name3
	full_key := generate_full_key(name)
	fmt.Println("The client full secret key is generated: ", full_key)
	ctx, cancell := context.WithTimeout(context.Background(), time.Second)
	defer cancell()

	r, err := c.SayHello3(ctx, &pb.Message3Request{Name: "ok"})
	if err != nil {
		log.Fatalf("Could not greet: %v", err)
	}

	log.Printf("Greeting: %s", r.Message)

}

func generate_part_key(key string) string {
	url := "http://172.20.20.60:8091/partial-key/" + key
	req, _ := http.NewRequest("POST", url, nil)
	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	//fmt.Println(string(body))

	return string(body)
}

func generate_full_key(key string) string {
	url := "http://172.20.20.60:8091/partial-key/" + key
	req, _ := http.NewRequest("POST", url, nil)
	res, _ := http.DefaultClient.Do(req)

	defer res.Body.Close()
	body, _ := ioutil.ReadAll(res.Body)
	//fmt.Println(string(body))

	return string(body)
}
