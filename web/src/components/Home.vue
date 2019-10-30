<template>
  <el-container>
  <el-header class="header">
      <div class="header-left">热榜聚合</div>
  </el-header>
  <el-main>
    <el-container class="hot-list">
      <el-row class="btn-row"> 
        <el-button class="select-type-btn" @click="getTypeList('zhihu')">知乎</el-button>
        <el-button class="select-type-btn" @click="getTypeList('v2ex')">v2ex</el-button>
      </el-row>
    </el-container>
    <el-divider></el-divider>
    <el-container>
      <div class="list-container" v-loading="loading">
        <div class="list-item" v-for="(item , index) in items" :key="item">
          <el-row>
            <!-- <div class="item-index">
              
            </div> -->
            <div class="item-title">
              <a :href="item.url" class="title-container"><em class="item-index">{{++index}}</em>{{item.title}}</a>
            </div>
          </el-row>
        </div>
      </div>
    </el-container>
  </el-main>
  <el-footer></el-footer>
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
  background-color: #f6f6f6
}
.btn-row{
  margin: 10px 0;
}
.item-index{
  float: left;
  text-align: center;
  margin: 0 26px 0 5px;
  display: block;
}

em{
  font-style: italic;
}
.title-container{
  display: block;
  padding: 0 12px;
  color: #363636;
  font-weight: 700;
  text-decoration: none;
}
.hot-list{
  position: sticky;
  z-index: 9;
  top: 0;
  border-bottom: 1px solid #ebebeb;
}
.item-title{
  float: left;
  color: black;
  
}


.list-container{
  width: 100%;
  min-height: 200px;
}

.list-item{
  border-bottom: 1px solid #ebebeb;
}

.header{
  background-color: #0078ff;
  height: 60px;
  text-align: center;
}
.header-left{
  float: left;
  height:60px;
  line-height: 60px;
  text-align: center;
  margin-left: 3px;
  color: azure;
}

.el-main{
  padding: 0px
}
</style>