<template>
  <div id="home" class="big-bg">
    <h1>Would you like to give shape to your memories?</h1>
    <v-btn
      large
      min-width="150"
      :loading="loading3"
      :disabled="loading3"
      color="blue-grey"
      class="ma-2 white--text"
      @click="loader = 'loading3'"
    >
      Registration
    </v-btn>
    <v-btn
      large
      min-width="200"
      :loading="loading3"
      :disabled="loading3"
      color="blue-grey"
      class="ma-2 white--text"
      @click="loader = 'loading3'"
    >
      login
    </v-btn>
  </div>
</template>

<style lang="scss" scoped>
@import '../assets/ress/ress.min.css';
/* 大きな背景画像 */
#home {
    background-image: url(../assets/images/image_1.jpg);
    min-height: 100vh;
    text-align: center;
    padding-top: 40vh;
}
.big-bg {
    background-size: cover;  /*縦横比を固定したまま画面いっぱいに画像を広げる*/
    background-position: center top;  /*画像を中央上部に配置*/
    background-repeat: no-repeat;  /*画像を繰り返さない*/
} 
h1 {
  color: #FFF;
  font-size: 3rem;
  padding-bottom: 30px;
}   
</style>