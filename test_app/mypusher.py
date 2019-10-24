import pusher

channels_client = pusher.Pusher(
  app_id='886771',
  key='0609171af1b2b00ee8f0',
  secret='f5109397c49eed39f0bc',
  cluster='us3',
  ssl=True
)

channels_client.trigger('my-channel', 'my-event', {'message': 'hello world'})