var page=require('webpage').create();
page.viewportSize={width:1024,height:768};
page.clipRect={top:0,left:0,width:1024,height:768};
page.open('http://github.com/',function(){
  page.render('github.png');
  phantom.exit();
})
