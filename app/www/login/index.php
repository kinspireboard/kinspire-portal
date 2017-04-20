<?php
session_start();
if ((isset($_SESSION['login']) && $_SESSION['login'] != '')) {
  header ("Location: ../");
}
?>
<head>
  <?php require $_SERVER['DOCUMENT_ROOT']."/includes/head.php"; ?>
  <title>Kinspire's Portal</title>
</head>
<body>
  <?php require $_SERVER['DOCUMENT_ROOT']."/includes/main-menu.php"; ?>
  <div class="portal-content">
    <div class="portal-header">
      <div class="portal-title portal-title-home">Kinspire's Portal</div>
    </div>
    <div class="portal-body">
      <div class="login-area">
        <form method="post" action="login.php">
          <input class="login-email" type="email" name="email" placeholder="email"/>
          <input class="login-password" type="password" name="password" placeholder="pass"/>
          <button type="submit" name="login" class="login-button">Log in</button>
          <button type="submit" name="signup" class="login-button">Sign up</button>
        </form>
      </div>
      <div>
        Use this: username = test@test.org, password = test
      </div>
    </div>
  </div>
  <?php require $_SERVER['DOCUMENT_ROOT']."/includes/footer.php"; ?>
</body>
