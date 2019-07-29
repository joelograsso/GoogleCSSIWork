<html>

<head>
  <title>Welcome to Memegen</title>
  <link rel='stylesheet' href="css/style.css" />
</head>

<body>
  <h1>Here are all created memes</h1>
  {% for i in storedMemes %}

  {{i.memeTextTop}}
  <br>
  <img src={{i.memeUrl}}>
  <br>
  {{i.memeTextBottom}}
  <br>

  {% endfor %}
</body>

</html>
