%% @author 15146
%% @doc @todo Add description to master.
%% C:\Users\Dhruvi\eclipse-workspace\COMP6411\src

-module(exchange).
-export([start/0,listen/0]).

print([Head|Tail]) ->
	{Sender,Reciever} = Head,
	io:fwrite("~w: ~w\n",[Sender,Reciever]),
	print(Tail);
print([]) -> io:fwrite("\n").
	
calls(MID,Sender,[Head1|Tail1]) ->
	SID = whereis(Sender),
	SID! {MID,Sender,Head1},
	calls(MID,Sender,Tail1);
calls(_,_,[]) -> io:fwrite("").

getpair(MID,[Head|Tail]) ->
	{Sender,Recievers} = Head,
	[Head1|Tail1] = Recievers,
	register(Sender, spawn(calling, receiver, [Sender])),
	calls(MID,Sender,[Head1|Tail1]),
	getpair(MID,Tail);
getpair(MID,[]) -> io:fwrite("").

listen() ->
	receive
		{s, Sname, Rname, Time} ->
			io:fwrite("~w received intro message from ~w [~w]~n",[Rname,Sname,Time]),
			listen();
		{r, Sname, Rname, Time} ->
			io:fwrite("~w received reply message from ~w [~w]~n",[Rname,Sname,Time]),
			listen();
		{n, Name} ->
			io:fwrite("process ~w has received no calls for 5 seconds, ending...~n",[Name]),
			listen()
	after 10000 ->
			io:fwrite("master has received no replies for 10 seconds, ending...~n"),
			exit(done)
	end.

start() -> 
	{_, C}=file:consult("calls.txt"),
	io:fwrite("** calls to be made **\n"),
	[Head|Tail] = C,
    print([Head|Tail]),
	MID = spawn(exchange, listen, []),
	getpair(MID,[Head|Tail]).
		
