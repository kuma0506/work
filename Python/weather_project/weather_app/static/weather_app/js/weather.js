$('#Every_6_hours').click(function(){
  $.ajax({
             url: '/every_hours_ajax/',
             method: "GET",
             // プレーンテキストを受信（他にはhtml、xml、script、json、jsonp等）
             dataType: 'text',
             // リクエストパラメータ「?param1=いろはに&param2=ほへと&param3=ちりぬるを」
             data: {
                 time: '6',
                 countryId: $('#Every_6_hours').val()
             },
             timeout: 10000,
         })
         .done(function(args) {
             // 『6時間ごとの予報』ボタンの背景色、文字色を変更
             document.getElementById('Every_6_hours').style.backgroundColor = '#0099FF';
             document.getElementById('Every_6_hours').style.color = '#FFFFFF';
             // 『3時間ごとの予報』ボタンの背景色、文字色を変更
             document.getElementById('Every_3_hours').style.backgroundColor = '#FFFFFF';
             document.getElementById('Every_3_hours').style.color = '#777777';
             // 通信成功時の処理を記述
             // 戻り値をJSONに変換
             const obj = JSON.parse(args);
             // 項目にセットする
             $('#days_01').text(obj.days_01)
             $('#days_02').text(obj.days_02)
             $('#days_03').text(obj.days_03)
             $('#days_04').text(obj.days_04)
             $('#days_05').text(obj.days_05)
             $('#days_06').text(obj.days_06)
             $('#days_07').text(obj.days_07)
             $('#days_08').text(obj.days_08)
             $('#days_09').text(obj.days_09)
             $('#days_10').text(obj.days_10)
             $('#times_01').text(obj.times_01)
             $('#times_02').text(obj.times_02)
             $('#times_03').text(obj.times_03)
             $('#times_04').text(obj.times_04)
             $('#times_05').text(obj.times_05)
             $('#times_06').text(obj.times_06)
             $('#times_07').text(obj.times_07)
             $('#times_08').text(obj.times_08)
             $('#times_09').text(obj.times_09)
             $('#times_10').text(obj.times_10)
             document.getElementById("icon_01").src = "http://openweathermap.org/img/w/"+obj.icon_01+".png"
             document.getElementById("icon_02").src = "http://openweathermap.org/img/w/"+obj.icon_02+".png"
             document.getElementById("icon_03").src = "http://openweathermap.org/img/w/"+obj.icon_03+".png"
             document.getElementById("icon_04").src = "http://openweathermap.org/img/w/"+obj.icon_04+".png"
             document.getElementById("icon_05").src = "http://openweathermap.org/img/w/"+obj.icon_05+".png"
             document.getElementById("icon_06").src = "http://openweathermap.org/img/w/"+obj.icon_06+".png"
             document.getElementById("icon_07").src = "http://openweathermap.org/img/w/"+obj.icon_07+".png"
             document.getElementById("icon_08").src = "http://openweathermap.org/img/w/"+obj.icon_08+".png"
             document.getElementById("icon_09").src = "http://openweathermap.org/img/w/"+obj.icon_09+".png"
             document.getElementById("icon_10").src = "http://openweathermap.org/img/w/"+obj.icon_10+".png"
             $('#temp_01').text(obj.temp_01)
             $('#temp_02').text(obj.temp_02)
             $('#temp_03').text(obj.temp_03)
             $('#temp_04').text(obj.temp_04)
             $('#temp_05').text(obj.temp_05)
             $('#temp_06').text(obj.temp_06)
             $('#temp_07').text(obj.temp_07)
             $('#temp_08').text(obj.temp_08)
             $('#temp_09').text(obj.temp_09)
             $('#temp_10').text(obj.temp_10)
             $('#humidity_01').text(obj.humidity_01)
             $('#humidity_02').text(obj.humidity_02)
             $('#humidity_03').text(obj.humidity_03)
             $('#humidity_04').text(obj.humidity_04)
             $('#humidity_05').text(obj.humidity_05)
             $('#humidity_06').text(obj.humidity_06)
             $('#humidity_07').text(obj.humidity_07)
             $('#humidity_08').text(obj.humidity_08)
             $('#humidity_09').text(obj.humidity_09)
             $('#humidity_10').text(obj.humidity_10)
             $('#speed_01').text(obj.speed_01)
             $('#speed_02').text(obj.speed_02)
             $('#speed_03').text(obj.speed_03)
             $('#speed_04').text(obj.speed_04)
             $('#speed_05').text(obj.speed_05)
             $('#speed_06').text(obj.speed_06)
             $('#speed_07').text(obj.speed_07)
             $('#speed_08').text(obj.speed_08)
             $('#speed_09').text(obj.speed_09)
             $('#speed_10').text(obj.speed_10)

         })
         .fail(function(args) {
             // 通信失敗時の処理を記述
             alert("error")
        });
});

$('#Every_3_hours').click(function(){
  $.ajax({
             url: '/every_hours_ajax/',
             method: "GET",
             // プレーンテキストを受信（他にはhtml、xml、script、json、jsonp等）
             dataType: 'text',
             // リクエストパラメータ「?param1=いろはに&param2=ほへと&param3=ちりぬるを」
             data: {
               time: '3',
               countryId: $('#Every_3_hours').val()
             },
             time: 10000,
         })
         .done(function(args) {
             // 通信成功時の処理を記述
             // 『3時間ごとの予報』ボタンの背景色、文字色を変更
             document.getElementById('Every_3_hours').style.backgroundColor = '#0099FF';
             document.getElementById('Every_3_hours').style.color = '#FFFFFF';
             // 『3時間ごとの予報』ボタンの背景色、文字色を変更
             document.getElementById('Every_6_hours').style.backgroundColor = '#FFFFFF';
             document.getElementById('Every_6_hours').style.color = '#777777';
             // 通信成功時の処理を記述
             // 戻り値をJSONに変換
             const obj = JSON.parse(args);
             // 項目にセットする
             $('#days_01').text(obj.days_01)
             $('#days_02').text(obj.days_02)
             $('#days_03').text(obj.days_03)
             $('#days_04').text(obj.days_04)
             $('#days_05').text(obj.days_05)
             $('#days_06').text(obj.days_06)
             $('#days_07').text(obj.days_07)
             $('#days_08').text(obj.days_08)
             $('#days_09').text(obj.days_09)
             $('#days_10').text(obj.days_10)
             $('#times_01').text(obj.times_01)
             $('#times_02').text(obj.times_02)
             $('#times_03').text(obj.times_03)
             $('#times_04').text(obj.times_04)
             $('#times_05').text(obj.times_05)
             $('#times_06').text(obj.times_06)
             $('#times_07').text(obj.times_07)
             $('#times_08').text(obj.times_08)
             $('#times_09').text(obj.times_09)
             $('#times_10').text(obj.times_10)
             document.getElementById("icon_01").src = "http://openweathermap.org/img/w/"+obj.icon_01+".png"
             document.getElementById("icon_02").src = "http://openweathermap.org/img/w/"+obj.icon_02+".png"
             document.getElementById("icon_03").src = "http://openweathermap.org/img/w/"+obj.icon_03+".png"
             document.getElementById("icon_04").src = "http://openweathermap.org/img/w/"+obj.icon_04+".png"
             document.getElementById("icon_05").src = "http://openweathermap.org/img/w/"+obj.icon_05+".png"
             document.getElementById("icon_06").src = "http://openweathermap.org/img/w/"+obj.icon_06+".png"
             document.getElementById("icon_07").src = "http://openweathermap.org/img/w/"+obj.icon_07+".png"
             document.getElementById("icon_08").src = "http://openweathermap.org/img/w/"+obj.icon_08+".png"
             document.getElementById("icon_09").src = "http://openweathermap.org/img/w/"+obj.icon_09+".png"
             document.getElementById("icon_10").src = "http://openweathermap.org/img/w/"+obj.icon_10+".png"
             $('#temp_01').text(obj.temp_01)
             $('#temp_02').text(obj.temp_02)
             $('#temp_03').text(obj.temp_03)
             $('#temp_04').text(obj.temp_04)
             $('#temp_05').text(obj.temp_05)
             $('#temp_06').text(obj.temp_06)
             $('#temp_07').text(obj.temp_07)
             $('#temp_08').text(obj.temp_08)
             $('#temp_09').text(obj.temp_09)
             $('#temp_10').text(obj.temp_10)
             $('#humidity_01').text(obj.humidity_01)
             $('#humidity_02').text(obj.humidity_02)
             $('#humidity_03').text(obj.humidity_03)
             $('#humidity_04').text(obj.humidity_04)
             $('#humidity_05').text(obj.humidity_05)
             $('#humidity_06').text(obj.humidity_06)
             $('#humidity_07').text(obj.humidity_07)
             $('#humidity_08').text(obj.humidity_08)
             $('#humidity_09').text(obj.humidity_09)
             $('#humidity_10').text(obj.humidity_10)
             $('#speed_01').text(obj.speed_01)
             $('#speed_02').text(obj.speed_02)
             $('#speed_03').text(obj.speed_03)
             $('#speed_04').text(obj.speed_04)
             $('#speed_05').text(obj.speed_05)
             $('#speed_06').text(obj.speed_06)
             $('#speed_07').text(obj.speed_07)
             $('#speed_08').text(obj.speed_08)
             $('#speed_09').text(obj.speed_09)
             $('#speed_10').text(obj.speed_10)

         })
         .fail(function(args) {
             // 通信失敗時の処理を記述
             alert("error")
        });

});
