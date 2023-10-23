package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"runtime"
)

// Handler to display system information in plain text
func systemInfoHandler(w http.ResponseWriter, r *http.Request) {
	fmt.Fprintf(w, "Operating System: %s\n", runtime.GOOS)
	fmt.Fprintf(w, "Architecture: %s\n", runtime.GOARCH)
	hostname, _ := os.Hostname()
	fmt.Fprintf(w, "Hostname: %s\n", hostname)
}

// Handler to display system information in JSON format
func systemInfoJSONHandler(w http.ResponseWriter, r *http.Request) {
	hostname, _ := os.Hostname()
	info := map[string]string{
		"Operating System": runtime.GOOS,
		"Architecture":     runtime.GOARCH,
		"Hostname":         hostname,
	}

	w.Header().Set("Content-Type", "application/json")
	json.NewEncoder(w).Encode(info)
}

func main() {
	http.HandleFunc("/systeminfo", systemInfoHandler)
	http.HandleFunc("/api/systeminfo", systemInfoJSONHandler)
	http.ListenAndServe(":8080", nil)
}
