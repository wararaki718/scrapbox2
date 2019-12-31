package main

import (
	"context"
	"fmt"
	"time"

	"google.golang.org/grpc"

	pb "./sample"
)

func main() {
	fmt.Println("client")

	conn, err := grpc.Dial("localhost:50051", grpc.WithInsecure(), grpc.WithBlock())
	if err != nil {
		fmt.Println("conneiction error")
	}
	defer conn.Close()
	client := pb.NewSampleServerClient(conn)

	ctx, cancel := context.WithTimeout(context.Background(), time.Second)
	defer cancel()

	response, err := client.SampleApi(ctx, &pb.SampleRequest{Name: "world"})
	if err != nil {
		fmt.Println("request error")
	}
	fmt.Println(response.GetMessage())
}
