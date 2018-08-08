var dict = {
  "Overview":"#Overview1",
  "Python":"#Python2",
  "Oracle":"#Oracle3",
  "Web":"#Web4"
};

function hide_show(key){
  $(dict[key]).show();

  for (var other_key in dict) {
      if (other_key != key) {
        $(dict[other_key]).hide();
      }
  }
}

$(document).ready(function(){
  $(".portfolio-button").click(function(obj){
    if (obj.target && obj.target.id){
      hide_show(obj.target.id);
    }
  })
});
