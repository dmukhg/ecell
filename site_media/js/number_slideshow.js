// Copyright 2010 htmldrive.net Inc.
/**
 * @projectHomepage: http://www.htmldrive.net/go/to/number-slideshow
 * @projectDescription: Number slideshow - simple and practical numbers image slideshow jQuery plugin.
 * @author htmldrive.net
 * @version 1.0
 * @license http://www.apache.org/licenses/LICENSE-2.0
 * More script and css style : htmldrive.net
 */
(function(a){
    a.fn.number_slideshow=function(p){
        var p=p||{};
        var n=p&&p.slideshow_autoplay?p.slideshow_autoplay:"enable";
        var o=p&&p.slideshow_time_interval?p.slideshow_time_interval:"500";
        var q=p&&p.slideshow_window_background_color?p.slideshow_window_background_color:"white";
        var r=p&&p.slideshow_window_padding?p.slideshow_window_padding:"5";
        var s=p&&p.slideshow_window_width?p.slideshow_window_width:"936";
        var t=p&&p.slideshow_window_height?p.slideshow_window_height:"357";
        var u=p&&p.slideshow_border_size?p.slideshow_border_size:"0";
        var v=p&&p.slideshow_border_color?p.slideshow_border_color:"white";
        var w=p&&p.slideshow_show_button?p.slideshow_show_button:"enable";
        var x=p&&p.slideshow_button_text_color?p.slideshow_button_text_color:"red";
        var z=p&&p.slideshow_button_background_color?p.slideshow_button_background_color:"black";
        var A=p&&p.slideshow_button_current_background_color?p.slideshow_button_current_background_color:"white";
        var B=p&&p.slideshow_button_border_color?p.slideshow_button_border_color:"blue";
        var C=p&&p.slideshow_button_border_size?p.slideshow_button_border_size:"2";
        r += "px";
        s += "px";
        t += "px";
        u += "px";
        C += "px";
        var D;
        var E=0;
        var F=a(this);
        var G=F.find("ul:first").children("li").length;
        if(F.find("ul").length==0||F.find("li").length==0){
            a.append("Require content");
            return null
        }
        F.show();
        F.find("ul:first").children("li").children("a").children("img").css("width",s).css("height",t);
        s_s_ul(F.find("ul:first"),r,s,t,u,v,q);
        s_s_n(F.find(".number_slideshow_nav"),x,w,z,A,B,C);
        F.find("ul:first").children("li").hide();
        play();
        F.find(".number_slideshow_nav").children("li").hover(function(){
            stop($(this))
        },function(){
            D=setTimeout(play,o)
        });
        function play(){
            if(n=="enable"){
                clearTimeout(D);
                F.find("ul:first").children("li").fadeOut();
                F.find("ul:first").children("li").eq(E).fadeIn();
                F.find(".number_slideshow_nav").children("li").css("background-color",z);
                F.find(".number_slideshow_nav").children("li").eq(E).css("background-color",A);
                E++;
                if(E>=G){
                    E=0
                }
                D=setTimeout(play,o)
            }else{
                F.find("ul:first").children("li").eq(E).fadeIn();
            }
        }
        function stop(a){
            clearTimeout(D);
            var b=a.parent().children().index(a);
            E=b+1;
            if(E>=G){
                E=0
            }
            F.find("ul:first").children("li").fadeOut();
            F.find("ul:first").children("li").eq(b).fadeIn();
            F.find(".number_slideshow_nav").children("li").css("background-color",z);
            F.find(".number_slideshow_nav").children("li").eq(b).css("background-color",A)
        }
        function s_s_ul(a,b,c,d,e,f,g){
            b=parseInt(b);
            c=parseInt(c);
            d=parseInt(d);
            e=parseInt(e);
            var h=c+e*2+b*2;
            var i=d+e*2+b*2;
            F.css("width",h);
            F.css("height",i);
            var j=d+"px";
            var k=c+"px";
            var l="border: "+f+" solid "+" "+'0'+"px; height:"+j+"; width:"+k+"; padding:"+b+"px; background-color:"+"#ffffff";
            a.attr("style",l)
        }
        function s_s_n(b,c,d,e,f,g,h){
            h=parseInt(h);
            var j=b.children("li");
            var a=j.children("a");
            a.css("color",c);
            var k="border: "+g+" solid "+" "+h+"px; background-color:"+e+";";
            j.attr("style",k);
            if(d!="enable"){
                b.hide()
            }
        }
    }
})(jQuery);
