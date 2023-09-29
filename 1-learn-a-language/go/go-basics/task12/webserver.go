package main

import (
	"fmt"
	"net/http"
	"os"
	"runtime"
)

func systemInfoHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Operating System: %s\n", runtime.GOOS)
	fmt.Fprintf(w, "Architecture: %s\n", runtime.GOARCH)
	hostname, _ := os.Hostname()
	fmt.Fprintf(w, "Hostname: %s\n", hostname)
}

func main() {
	http.HandleFunc("/systeminfo", systemInfoHandler)
	http.ListenAndServe(":8080", nil)
}
