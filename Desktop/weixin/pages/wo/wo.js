// pages/page wo/wo.js

//获取应用实例
const app = getApp()
var QQMapWX=require('../lib/qqmap-wx-jssdk.js');
var qqmapsdk;
Page({

  /**
   * 页面的初始数据
   */
  data: {
    a: ''
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that=this;
    that.setData({
      a: app.globalData.userInfo.avatarUrl
    })
    qqmapsdk = new QQMapWX({ key:'8123d1f85b4b987b4f5871eeda63bd3e'});
  },

  /**
   * 生命周期函数--监听页面初次渲染完成
   */
  onReady: function () {
  
  },
 
  /**
   * 生命周期函数--监听页面显示
   */
  onShow: function () {
  
  },

  /**
   * 生命周期函数--监听页面隐藏
   */
  onHide: function () {
  
  },

  /**
   * 生命周期函数--监听页面卸载
   */
  onUnload: function () {
  
  },
changeImg:function(){
  wx.chooseImage({
    count:1,
    sizeType:['original','compressed'],
    sourceType:['album','camera'],
    success: function(res) {
      var tem = res.tempFilePaths
      wx.uploadFile({
        url: 'https://www.gwx.fun/Dk/dk/insert',
        filePath: tem[0],
        name: 'user_img',
        formData:{
          user_name:'gwx'
        },
        success:function(e){
          var data=e.data
          console.log(data)
        }
      })
    },
  })
}
  ,
  location:function(){
    wx.getLocation({
      success: function(res) {
        console.log(res.latitude+":"+res.longitude)

        qqmapsdk.reverseGeocoder(
          {
              latitude:res.latitude,
              longitude: res.longitude,
           
          success:function(e){
              wx.showModal({
                title: '地址',
                content: e.result.address,
              })
          }
            
          }

        )
      },
    })


  }
  ,

  /**
   * 页面相关事件处理函数--监听用户下拉动作
   */
  onPullDownRefresh: function () {
  
  },
  /**
   * 页面上拉触底事件的处理函数
   */
  onReachBottom: function () {
  
  },

  /**
   * 用户点击右上角分享
   */
  onShareAppMessage: function () {
  
  },
  bindViewTap:function(){
    wx.login({
      success: res=>{
        this.setData({
          
        })
      }
    })
   
  }
})