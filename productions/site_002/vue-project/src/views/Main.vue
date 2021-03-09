<template>
  <v-app>
    <div id="div_1">
      <HeaderCom/>
    </div>
    <div id="div_2" class="big-bg">
      <v-row justify="center">
        <v-col
          cols="12"
          sm="6"
          md="4"
          class="d-flex flex-row align-baseline"
        >
          <v-text-field
            label="Search"
            solo
          >
          </v-text-field>
          <v-btn 
            color="blue-grey"
            class="white--text button_1"
            large
          >
          検索
          </v-btn>
        </v-col>
      </v-row>
    </div>
    <div id="div_3" class="d-flex child-flex">
      <v-card 
        class="card_1"
        max-width="200" 
      >
        <v-list
          nav
          dense
        >
          <v-list-item-group color="blue-grey">
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu1</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu2</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu3</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu4</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu5</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu6</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu7</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu8</a></v-list-item-title>
            </v-list-item>
            <v-list-item>
              <v-list-item-title><a href="#" class="grey--text">Menu9</a></v-list-item-title>
            </v-list-item>            
          </v-list-item-group>
        </v-list>
      </v-card>
      <v-row 
        class="row_1"
      >
        <v-col
          v-for="n in 9"
          :key="n"
          class="d-flex child-flex"
          cols="4"
        >
          <v-img
            :src="`https://picsum.photos/500/300?image=${n * 5 + 10}`"
            :lazy-src="`https://picsum.photos/10/6?image=${n * 5 + 10}`"
            aspect-ratio="1"
            class="grey lighten-2"
          >
            <template v-slot:placeholder>
              <v-row
                class="fill-height ma-0"
                align="center"
                justify="center"
              >
                <v-progress-circular
                  indeterminate
                  color="grey lighten-5"
                ></v-progress-circular>
              </v-row>
            </template>
          </v-img>
        </v-col>
      </v-row>
    </div>
    <div id="div_4">
      <FooterCom/>
    </div>
  </v-app>
</template>

<style lang="scss" scoped>
@import '../assets/ress/ress.min.css';
#div_2 {
  background-image: url(../assets/images/image_2.jpg);
  text-align: center;
  width: 100%;
  height: 50%;
  padding-top: 20vh;
  padding-bottom: 15vh;
  margin-top: 7vh;
}
#div_3 {
  padding: 4vh 6vw;
  background-color: #EEEEEE;
}
#div_4 {
  margin-top: 4vh;
}
.big-bg {
  background-size: cover;  /*縦横比を固定したまま画面いっぱいに画像を広げる*/
  background-position: center top;  /*画像を中央上部に配置*/
  background-repeat: no-repeat;  /*画像を繰り返さない*/
} 
.button_1 {
  font-size: 1.1rem;
}
.card_1 {
  margin-right: 40px;
}
a {
  display: block;
  text-decoration: none;
}

</style>

<script lang="ts">
import { Component, Vue } from 'vue-property-decorator';
import HeaderCom from '@/components/HeaderCom.vue';
import FooterCom from '@/components/FooterCom.vue';

@Component({
  components: {
    HeaderCom,
    FooterCom
  },
})
export default class Main extends Vue {
  data(){
    return {
    }
  }
}
</script>