var page=require('webpage').create();
page.open('http://cuiqincai.com',function(status){
  console.log("status:"+status);
  if(status=="success")
  {
    console.log("Save the picture.");
    page.render('example.png');
  }
  phantom.exit();
})
