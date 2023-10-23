package main

import (
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3"
)

func createBucket(sess *session.Session, bucketName string) {
	// Create S3 service client
	svc := s3.New(sess)

	// Create the S3 Bucket
	_, err := svc.CreateBucket(&s3.CreateBucketInput{
		Bucket: aws.String(bucketName),
	})
	if err != nil {
		log.Fatalf("Unable to create bucket %q, %v", bucketName, err)
	}

	// Wait until bucket is created before finishing
	fmt.Printf("Waiting for bucket %q to be created...\n", bucketName)
	err = svc.WaitUntilBucketExists(&s3.HeadBucketInput{
		Bucket: aws.String(bucketName),
	})
	if err != nil {
		log.Fatalf("Error occurred while waiting for bucket to be created, %v", bucketName)
	}

	fmt.Printf("Bucket %q successfully created\n", bucketName)
}

func main() {
	// Initialize a session
	sess, err := session.NewSession(&aws.Config{
		Region: aws.String("us-west-1"), // Change this to your preferred region
	})
	if err != nil {
		log.Fatalf("Failed to create session, %v", err)
	}

	// Specify the bucket name
	bucketName := "my-new-bucket-name" // Change this to your desired bucket name

	// Call the function to create the bucket
	createBucket(sess, bucketName)
}
