<!doctype html>
<html lang="ru">
<head>
  <meta charset="UTF-8">
  <meta
    name="viewport"
    content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0"
  >
  <meta http-equiv="X-UA-Compatible" content="ie=edge">
  <link rel="stylesheet" href="../static/css/style.css">
  <title>Расчет энергоэффективности умного дома</title>
</head>
<body>
  <header class="header">
    <div class="header__text">
      <h1>Расчитай энергоэффективность своего дома!</h1>
      <p>Реши проблему излишнего электропотребления самостоятельно!</p>
    </div>
  </header>
  <main>
    {% block content %}
    <h2 class="main__title">Выбери количество электрических приборов:</h2>
    <ul class="list" id="list">
      <!-- Задание №3 -->
      <li class="list__item">
        <a href={{lights + "/4" }}>
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>3-5 прибора</span></a>
      </li>
      <li class="list__item">
        <a href={{lights + "/7" }}>
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>6-8 приборов</span></a>
      </li>
      <li class="list__item">
        <a href={{lights + "/11" }}>
          <img class="item__img" src="../static/img/battery.svg" alt="battery">
          <span>10 и более</span></a>
      </li>
      <!--  -->
    </ul>
    {% endblock %}
  </main>
  <footer>

  </footer>
</body>
</html>
<li class="list__item">
  <a href="{{lights + "/1"}}">
    <img class="item__img" src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fimg.freepik.com%2Fpremium-photo%2Fgreen-grape-leaf-isolated-on-white-background-clipping-path_157837-2996.jpg&tbnid=tdcD1RXeM9yRAM&vet=12ahUKEwjc-KCI2P7_AhXPGBAIHcGlBnIQMyg2egQIARBr..i&imgrefurl=https%3A%2F%2Fru.freepik.com%2Ffree-photos-vectors%2F%25D0%25B4%25D1%2583%25D0%25B1%25D0%25BE%25D0%25B2%25D1%258B%25D0%25B9-%25D0%25BB%25D0%25B8%25D1%2581%25D1%2582&docid=B_CaHft9IBhHiM&w=489&h=626&q=%D0%BB%D0%B8%D1%81%D1%82&safe=active&ved=2ahUKEwjc-KCI2P7_AhXPGBAIHcGlBnIQMyg2egQIARBr" alt="battery">
    <span>0-1</span></a>
</li>
