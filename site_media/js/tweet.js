function relative_time(time_value) {
    var time_lt1min = 'less than 1 min ago';
    var time_1min = '1 min ago';
    var time_mins = '%1 mins ago';
    var time_1hour = '1 hour ago';
    var time_hours = '%1 hours ago';
    var time_1day = '1 day ago';
    var time_days = '%1 days ago';

    var values = time_value.split(" ");
    time_value = values[1] + " " + values[2] + ", " + values[5] + " " + values[3];
    var parsed_date = Date.parse(time_value);
    var relative_to = (arguments.length > 1) ? arguments[1] : new Date();
    var delta = parseInt((relative_to.getTime() - parsed_date) / 1000);
    delta = delta + (relative_to.getTimezoneOffset() * 60);

    if (delta < 60) {
        return time_lt1min;
    } else if(delta < 120) {
        return time_1min;
    } else if(delta < (60*60)) {
        return time_mins.replace('%1', (parseInt(delta / 60)).toString());
    } else if(delta < (120*60)) {
        return time_1hour;
    } else if(delta < (24*60*60)) {
        return time_hours.replace('%1', (parseInt(delta / 3600)).toString());
    } else if(delta < (48*60*60)) {
        return time_1day;
    } else {
        return time_days.replace('%1', (parseInt(delta / 86400)).toString());
    }
}

function twitterCallback1(twitters) {
    var statusHTML = [];
    var statusHTMLI = [];
    for (var i=0; i<twitters.length; i++){
        var username = twitters[i].user.screen_name;

        var FollowersCount = twitters[i].user.followers_count;
        var FriendsCount = twitters[i].user.friends_count;
        var ProfileImageUrl = twitters[i].user.profile_image_url;
        var StatusesCount = twitters[i].user.statuses_count;

        pic = twitters[i].user.profile_image_url;
        var status = twitters[i].text.replace(/((https?|s?ftp|ssh)\:\/\/[^"\s\<\>]*[^.,;'">\:\s\<\>\)\]\!])/g, function(url) {
                return '<a href="'+url+'">'+url+'</a>';
                }).replace(/\B@([_a-z0-9]+)/ig, function(reply) {
                    return  reply.charAt(0)+'<a href="http://twitter.com/'+reply.substring(1)+'">'+reply.substring(1)+'</a>';
                    });
        if (i==0){
            statusHTMLI.push('<a href="http://www.twitter.com/'+username+'"><img align="left" src='+ProfileImageUrl+'></a><b>Tweet Us at <a href="http://www.twitter.com/'+username+'">'+username+'</b></a><br/>Followers: '+FollowersCount+' | Following: '+FriendsCount+' | Tweets: '+StatusesCount+'');
        }
        statusHTML.push('<li><div class="timeago"><a href="http://twitter.com/'+username+'/statuses/'+twitters[i].id+'">'+relative_time(twitters[i].created_at)+'</a></div><span>'+status+'</span></li>');
    }
    document.getElementById('twitter_info_ws').innerHTML = statusHTMLI.join('');
    document.getElementById('twitter_update_list_ws').innerHTML = statusHTML.join('');
}
