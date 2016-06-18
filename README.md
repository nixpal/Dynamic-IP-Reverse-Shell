# DDNS-NOMORE
Reverse tunnel with DYNAMIC IP, NO DDNS Required

You ever wondered how to connect to your PC at work but you have no control over your firewall. You can't portforward anything. Well of course we can do that with reverse connection, we all know that. But now I'm doing this as your IP is Dynamic and changing every time you reboot your router.

How it works:

We will run python script to retrieve emails from your inbox, whether it is a gmail or not doesn't matter. We will use Imaplib for this to work.

After reading inbox messages we will look for a certain message with certain subject when it matches our subject, the script will get the body of the message for you, and that's for sure will be your IP ADDRESS. It's like you are sending your new IP ADDRESS to your email and your script is listening there waiting for you. It will then read the Body(IP ADDRESS) output that to a text file then execute a predefined shell script.

The shell script will read that text file, get the ip address to a variable. Connect to that with a reverse shell tunnel, then you can connect on the same tunnel with Localhost and Localport(tunnel port) as your remote host, remote port.

That's it you got a shell to your work.

I didn't optimize the script to check for seen/unseen flag yet, and check again for new incoming connections, you can edit that, add your code, or wait me to add that later.

Yes, you can do that without the shell script, by adding Subprocess module to the script, but it's just way more simple to execute the shell script and that's it.

