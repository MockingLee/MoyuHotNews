import axios from 'axios'
import router from './router/index'

axios.default.timeout = 5000
axios.defaults.headers.post['Content-Type'] = 'application/json'

const instance = axios.create();
instance.defaults.headers.post['Content-Type'] = 'application/json'

export default{
  getTypeList(data){
    return instance.get('/api/typelist', {
      params :{
        type: data
      }
    })
  }
}