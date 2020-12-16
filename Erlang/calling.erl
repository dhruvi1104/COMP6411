%% @author 15146
%% @doc @todo Add description to calling.


-module(calling).
-export([receiver/1]).

receiver(SenderName) ->
	receive
		{MID, Sender, Receiver} ->
			{_,_,TS} = now(),
          	timer:sleep(rand:uniform(100)),
			MID! {s, Sender, Receiver, TS},
			Receiver ! {r, MID, Receiver, Sender, TS},
			receiver(Sender);
		{r, MID, Sender, Receiver, TS} ->
            timer:sleep(rand:uniform(100)),
			MID! {r, Sender, Receiver, TS},
			receiver(Sender)
	after 5000 ->
		io:fwrite("process ~w has received no calls for 5 seconds, ending...~n",[SenderName]),
		exit(done)
	end.
