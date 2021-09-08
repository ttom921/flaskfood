siege -c20 -t60  -v http://127.0.0.1:5000/long-polling
siege -c100 -t60  -v http://10.4.7.131/long-polling
curl http://10.4.7.131/long-polling