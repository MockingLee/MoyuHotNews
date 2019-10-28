<template>
  <el-container>
  <el-header>Header</el-header>
  <el-main>
    <el-container>
      <el-row>
        <el-button class="select-type-btn" @click="getTypeList('zhihu')">知乎</el-button>
      </el-row>
    </el-container>
    <el-divider></el-divider>
    <el-container>
      <div class="list-container" v-loading="loading">
        <div class="list-item" v-for="(item , index) in items" :key="item">
          <el-row>
            <div class="item-index">
              {{++index}}
            </div>
            <div class="item-title">
              <a :href="item.url">{{item.title}}</a>
            </div>
          </el-row>
        </div>
      </div>
    </el-container>
  </el-main>
  <el-footer>Footer</el-footer>
</el-container>
</template>

<script>
import api from '../axios'

export default {
  name: 'Home',
  data(){
    return{
      loading: false,
      items: []
    }
  },
  methods:{
    getTypeList(data){
      console.log(data)
      this.loading = true
      api.getTypeList(data).then(({
        data
      }) => {
        console.log(data)
        if(data.code === 200){
          this.items = data.data
          this.loading = false
        }
      })
    }
  },
  mounted(){

  }
}
</script>

<style>
.select-type-btn{
  background-color: #DCDFE6
}
.item-index{
  float: left;
  text-align: center;
  height: 100%;
  width: 57px;
  
}
.item-title{
  float: left;
}
</style>