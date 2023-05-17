package

main
import (
"crypto/rand"
"fmt"
"os"
)
func main() {
if len(os.Args) > 1 {
fmt.Println("Error: this program does not accept command-line arguments")
return
}
b := make([]byte, 16)
_, err := rand.Read(b)
if err != nil {
fmt.Println("Error:", err)
return
}
fmt.Printf("%x\n", b)
}
