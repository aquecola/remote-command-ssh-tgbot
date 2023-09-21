# How to use it:

* Generate id_rsa key, if you need it and copy key to your virtual-machine:

`ssh-keygen`
`ssh-copy-id root@192.168.4.223`
`copy id_rsa private key in app folder and rename it "remote_rsa"`

* Make docker image:

`docker build -t mytelegrambot-image .`

*  Run docker container:

`docker run -d \
  -e BOT_TOKEN=YOUR_BOT_TOKEN \
  -e SSH_HOST=192.168.7.133 \
  -e SSH_PORT=5500 \
  -e SSH_USERNAME=admin \
  -e ALLOWED_CHAT_ID=123456789 \
  --name mytelegrambot-container \
  mytelegrambot-image
`