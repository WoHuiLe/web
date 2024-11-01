<template>
  <div id="app">
    <el-button color="#626aef" @click="startTest" :disabled="isTesting">开始测试</el-button>
    <el-button color="#626aef" @click="getData">获取数据</el-button>
  </div>
</template>

<script>
// import { Swal } from "sweetalert2"; //这种方式不能正常引入sweetalert2
import Swal from 'sweetalert2/dist/sweetalert2.all.js';
import axios from 'axios';

export default {
  data() {
    return {
      isTesting: false // 添加一个标志变量
    }
  },
  methods: {
    async startTest() {
      if (this.isTesting) return; // 如果已经在测试中，直接返回
      this.isTesting = true; // 设置为正在测试
      console.log('开始测试le')
      try {
        await Swal.fire({
          title: '成功啦！',
          text: '这是一个简单的SweetAlert2示例。',
          icon: 'success'
        });
      } catch (error) {
        console.error('Swal.fire 调用失败:', error);
      } finally {
        this.isTesting = false; // 无论成功还是失败，都重置标志变量
      }
    },
    async getData() {
      console.log('get_Data')
      try {
      const response = await axios.get("http://10.10.6.27:6111/Data/data");
      console.log(response.data);
    } catch (error) {
      console.error('请求失败:', error);
    }
    }
  }
}
</script>

<style>

</style>