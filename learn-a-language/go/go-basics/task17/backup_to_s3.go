package main

import (
	"fmt"
	"log"
	"os"
	"path/filepath"

	"github.com/aws/aws-sdk-go/aws"
	"github.com/aws/aws-sdk-go/aws/session"
	"github.com/aws/aws-sdk-go/service/s3/s3manager"
)

func uploadToS3(sess *session.Session, bucketName, dirPath string) {
	uploader := s3manager.NewUploader(sess)

	err := filepath.Walk(dirPath, func(path string, info os.FileInfo, err error) error {
		if !info.IsDir() {
			file, err := os.Open(path)
			if err != nil {
				return err
			}
			defer file.Close()

			_, err = uploader.Upload(&s3manager.UploadInput{
				Bucket: aws.String(bucketName),
				Key:    aws.String(path),
				Body:   file,
			})
			if err != nil {
				return err
			}
			fmt.Printf("Successfully uploaded %s to %s\n", path, bucketName)
		}
		return nil
	})

	if err != nil {
		log.Fatalf("Error uploading directory to S3: %v", err)
	}
}

func main() {
	// Initialize a session
	sess, err := session.NewSession(&aws.Config{
		Region: aws.String("us-west-1"), // Adjust to your AWS region
	})
	if err != nil {
		log.Fatalf("Failed to create session, %v", err)
	}

	// Specify the bucket name and directory path
	bucketName := "your-s3-bucket-name"
	dirPath := "/path/to/your/directory"

	// Call the function to upload the directory to S3
	uploadToS3(sess, bucketName, dirPath)
}
