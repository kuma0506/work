<template>
<body>
  <h3>検索結果詳細</h3>
  <v-col
    cols="12"
    md="3"
  >
    <v-text-field
      label="登録者ID"
      v-model="id"
      :disabled="isDisabled"
    ></v-text-field>
    <v-text-field
      label="登録者名"
      v-model="name"
    ></v-text-field>    
  </v-col>
<v-row>
  <v-col 
    md="1"
  >
    <v-btn v-on:click="updateButton"
      depressed
      color="primary"
    >
      更新
    </v-btn>
    <v-btn v-on:click="deleteButton"
      depressed
      color="error"
    >
      削除
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

export default class Detail extends Vue {

  id: String = "";
  name: String = "";
  items: any[] = [];

  data() {
    return {
      id:"",
      name:"",
      isDisabled: true
    }
  }
  created() {
    var id = this.$route.params.id
    axios.get('http://localhost:8080/detail?id='+ id)
      .then(response => {
        this.$data.id = response.data.id
        this.$data.name = response.data.name
      })
      .catch(e => {
      })
  }
  updateButton() {
    var id = this.$data.id
    var name = this.$data.name
    axios.get('http://localhost:8080/update?id='+ id + '&name=' + name)
  }
  deleteButton() {
    var id = this.$data.id
    axios.get('http://localhost:8080/delete?id='+ id)
  }
  indexButton() {
    this.$router.push("/")
  }
}
</script>
