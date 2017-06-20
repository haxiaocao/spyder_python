var url='http://www.cuiqingcai.com'
var page=require('webpage').create();
page.onResourceRequested=function(request){
  console.log('Request '+JSON.stringify(request,undefined,4));

}
page.onResoureReceived=function(response){
  console.log('Receive '+JSON.stringify(response,undefined,4));
}
page.open(ulr);
phantom.exit();
