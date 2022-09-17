# noNetTrafficShutdown
If there is no network traffic for 10 (Now 20) Minutes your PC will be shutdown.
(Timer changed to 20 minutes to allow for large steam updates.)

I have a large steam collection and a terrible internet connection, this program lets me leave my PC on overnight, the PC will shutdown once all the downloads/updates are completed.

If transfer speed drops below 200k/s a 10 minute countedown will start.
If the transfer speed increases above 200k/s the countdown will pause for 10 seconds, this is to allow for an "blips" in the connection, if the speed drops below 200k/s within the 10 seconds the countdown will continue.
If the speed is still above 200k/s after 10 seconds the countdown is reset to 10 minutes.


