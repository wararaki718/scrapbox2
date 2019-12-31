package main

import (
	"context"
	"fmt"
	"net"

	"google.golang.org/grpc"

	pb "./sample"
)

type SampleServer struct {
}

func (s *SampleServer) SampleApi(ctx context.Context, in *pb.SampleRequest) (*pb.SampleResponse, error) {
	fmt.Println("recieve")
	return &pb.SampleResponse{Message: "hello " + in.GetName()}, nil
}

func main() {
	fmt.Println("server")

	listenPort, err := net.Listen("tcp", ":50051")
	if err != nil {
		fmt.Println("failed to connect")
	}

	server := grpc.NewServer()
	pb.RegisterSampleServerServer(server, &SampleServer{})
	if err := server.Serve(listenPort); err != nil {
		fmt.Println("failed to serve")
	}
}
