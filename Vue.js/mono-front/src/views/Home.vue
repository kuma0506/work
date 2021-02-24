<template>
<body>
  <h3>登録者一覧</h3>
  <v-simple-table>
    <template v-slot:default>
      <thead>
        <tr>
          <th class="text-left">
            登録者ID
          </th>
          <th class="text-left">
            登録者名
          </th>
        </tr>
      </thead>
      <tbody>
        <tr
          v-for="item in items" 
          :key="item.id"
        >
          <td><router-link :to="`/detail/${item.id}`">{{ item.id}}</router-link></td>
          <td>{{ item.name }}</td>
        </tr>
      </tbody>
    </template>
  </v-simple-table>
    <router-link to="/insert">
    <v-btn v-on:click="inputButton"
      class="ma-2"
      :loading="loading"
      :disabled="loading"
      color="secondary"
      @click="loader = 'loading'"
    >登録画面
    </v-btn>
    </router-link>
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

export default class Home extends Vue {

  items: any[] = [];
  created() {
    this.items = axiosItem()
    function axiosItem() {
      let item: any[] = []
      axios.get('http://localhost:8080/')
        .then(function (response) {
          console.log("Spring Access done");
          for (let i=0; i<response.data.length; i++){
            item.push({"id":response.data[i].id,"name":response.data[i].name})
          }
        })
        .catch(function (error) {
          console.log("Spring Access not done");
        })
        .finally(function () {
        }); 
      return item
    }  
  }
  inputbutton() {

  }
}
</script>
