
# tweet in your terminal! (EASY)

## Environment
- Unix
- Mac OS
- Install python in your device

## setup
- Go to a Twitter Development Web, Apply API!
- take a consumer-key, consumer-secret-key, token, secret-token
- Download this file. just one file
- Library Install `$ pip install python-twitter`
- In your terminal, type bellow command.

```
$ export TWITTER_CONSUMER_KEY="{consumer-key}"
$ export TWITTER_CONSUMER_SECRET_KEY="{consumer-secret-key}"
$ export TWITTER_TOKEN="{token}"
$ export TWITTER_TOKEN_SECRET="{secret-token}"
```

That's all!!
The following command is running command.

```
python post_twitter.py hogehoge
```

if you want to tweet just bellow command,
```
$ tweet hogehoge
```
write path in your bash file.*(.bashrc  or .bash_profile)
```bashrc
alias tweet='python /{absolute path}/post_twitter.py'
```

If you modify bash file, type ` $ source ~/.bashrc` or restart terminal.

Well done!
Now you can tweet in your terminal! ' $ tweet hogehoge!'
