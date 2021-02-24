<template>
  <div id="home" class="big-bg">
  </div>
</template>

<style lang="scss" scoped>
@import '../assets/ress/ress.min.css';
/* 大きな背景画像 */
.big-bg {
    background-size: cover;  /*縦横比を固定したまま画面いっぱいに画像を広げる*/
    background-position: center top;  /*画像を中央上部に配置*/
    background-repeat: no-repeat;  /*画像を繰り返さない*/
}
#home {
    background-image: url(../assets/images/image_1.jpg);
    min-height: 100vh;
}
</style>