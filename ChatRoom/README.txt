python server.py
python client.py

bind on localhost ,port 9990.

both server and client can input "exit" to exit. But CAN NOT exit a server when you just start one.

1 server_gevent.py/client_gevent.py
(1) using gevent socket ;
(2) CLIENT using select , timeout set 0 ;
(3) add time prefix brefore message;
(4) add client num at the end of message when someone in and out ;
(5) while len(client_list) == 0. SERVER can select between 'continue' and 'exit';
(6) client_list only can change by one greenlet .


