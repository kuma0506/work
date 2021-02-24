<template>
  <body>
    <h3>登録画面</h3>
  <v-col
    cols="12"
    md="3"
  >
    <v-text-field
      label="登録者名"
      v-model="name"
    ></v-text-field>    
  </v-col>
  <p class="red--text">{{ errors }}</p>
  <v-row>
  <v-col 
    md="1"
  >
    <v-btn v-on:click="inputButton"
      depressed
      color="#a9a9a9"
    >
      登録
    </v-btn>
    <v-btn v-on:click="indexButton"
      depressed
      color="#b0c4de"
    >
      一覧
    </v-btn>
  </v-col>
</v-row>  
  </body>
</template>

<script src="https://cdn.jsdelivr.net/npm/axios/dist/axios.min.js"></script>
<script src="https://unpkg.com/axios/dist/axios.min.js"></script>
<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HelloWorld from '@/components/HelloWorld.vue'; // @ is an alias to /src
import axios from 'axios'

@Component({
  components: {
  },
})

export default class Input extends Vue {

  items: any[] = [];
  //入力値を取得するためにdataを用意する必要がある
  data() {
    return {
      name:"",
      errors: "",
    }
  }
  inputButton() {
    var params = this.$data.name
    //入力されたメッセージが「空文字 or 空文字列」の場合、エラーとする
    if(!params.trim()){
      //エラーメッセージ設定
      this.$data.errors = "登録者名を入力してください"
    } else {
      //エラーメッセージ初期化
      this.$data.errors = ""
      this.items = axiosItem()

      function axiosItem() {
        let item: any[] = []
        axios.get('http://localhost:8080/insert?name='+ params)
          .then(function (response) {
            console.log("登録完了");
          })
          .catch(function (error) {
          })
          .finally(function () {
          }); 
          return item
      }
    }
  }
  indexButton() {
    this.$router.push("/")
  }
}
</script>
