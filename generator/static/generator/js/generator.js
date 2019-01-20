function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      var cookies = document.cookie.split(';');
      for (var i = 0; i < cookies.length; i++) {
        var cookie = jQuery.trim(cookies[i]);
        // Does this cookie string begin with the name we want?
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  var csrftoken = getCookie('csrftoken');
  
  function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
  }
  $.ajaxSetup({
    beforeSend: function (xhr, settings) {
      if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
        xhr.setRequestHeader("X-CSRFToken", csrftoken);
      }
    }
  });

$(function () {
  init();
  
    var $main_category = $('.main_category');
    var $sub_category = $('.sub_category'); //各セレクトの要素を変数に入れます。
    var $sub_category_2 = $('.sub_category_2');
    var $length = $('.length');
    var $skirt_length = $('.skirt_length');
    var $leg = $('.leg');
    var $design = $('.design');
    var $fit = $('.fit');
    var $neck = $('.neck');
    var $coller = $('.coller');
    var $zipbutton = $('.zipbutton');
    var $effect = $('.effect');

    var originalSubCategory = $sub_category.html();
    var originalSubCategory2 = $sub_category_2.html(); //後のイベントで、不要なoption要素を削除するため、オリジナルをとっておく
    var fitOriginal = $fit.html();
    var designOriginal = $design.html();
    var neckOriginal = $neck.html();
    var collerOriginal = $coller.html();
    var zipbuttonOriginal = $zipbutton.html();
    var lengthOriginal = $length.html();
    var skirtLengthOriginal = $skirt_length.html();
    var legOriginal = $leg.html();
    var effectOriginal = $effect.html();


    var condition_sub_category = [
      { element: $length, original: $length.html() },
      { element: $skirt_length, original: $skirt_length.html() },
      { element: $leg, original: $leg.html() },
      { element: $design, original: $design.html() },
      { element: $fit, original: $fit.html() }
    ];

    var condition_sub_category_2 = [{ element: $neck, original: $neck.html() },
    { element: $coller, original: $coller.html() },
    { element: $zipbutton, original: $zipbutton.html() },
    { element: $effect, original: $effect.html() }];


    //地方側のselect要素が変更になるとイベントが発生
    $('.main_category').change(function () {

      //選択された地方のvalueを取得し変数に入れる
      var valMainCategory = $(this).val();
      var valSubCategory = $('.sub_category').val();
      var valSubCategory2 = $('.sub_category_2').val();

      //削除された要素をもとに戻すため.html(original)を入れておく
      $sub_category.html(originalSubCategory).find('option').each(function () {
        var dataValSubCategory = $(this).data('val'); //data-valの値を取得
        //valueと異なるdata-valを持つ要素を削除
        if (valMainCategory != dataValSubCategory) {
          $(this).not(':first-child').remove();
        }
      });

      $sub_category_2.html(originalSubCategory2).find('option').each(function () {
        var dataValSubCategory2 = $(this).data('val'); //data-valの値を取得
        //valueと異なるdata-valを持つ要素を削除
        if (valSubCategory != dataValSubCategory2) {
          $(this).not(':first-child').remove();
        }
      });

      $.each(condition_sub_category, function (index, val) {
        //削除された要素をもとに戻すため.html(original)を入れておく
        val.element.html(val.original).find('option').each(function () {

          var dataValSubCategory2 = $(this).data('val'); //data-valの値を取得
          //valueと異なるdata-valを持つ要素を削除
          if (valSubCategory != dataValSubCategory2) {
            $(this).not(':first-child').remove();
          }

        });
      });

      $.each(condition_sub_category_2, function (index, val) {
        //削除された要素をもとに戻すため.html(original)を入れておく
        val.element.html(val.original).find('option').each(function () {

          var dataVal = $(this).data('val'); //data-valの値を取得
          //valueと異なるdata-valを持つ要素を削除
          if (valSubCategory2 != dataVal) {
            $(this).not(':first-child').remove();
          }

        });
      });

      //メインカテゴリ（性別）のselect要素が未選択の場合、その他をdisabledにする
      if ($(this).val() == "") {
        $sub_category.attr('disabled', 'disabled');
        $sub_category_2.attr('disabled', 'disabled');

      } else {
        $sub_category.removeAttr('disabled');
        $sub_category_2.attr('disabled', 'disabled');
      }
      $.each(condition_sub_category, function (index, val) {
        val.element.attr('disabled', 'disabled');
      });
      $.each(condition_sub_category_2, function (index, val) {
        val.element.attr('disabled', 'disabled');
      });
    });


    //サブカテゴリ（トップスかパンツか）のselect要素が変更になるとイベントが発生
    $('.sub_category').change(function () {

      //選択されたサブカテゴリのvalueを取得し変数に入れる
      var valSubCategory = $(this).val();
      var valSubCategory2 = $('.sub_category_2').val();

      //削除された要素をもとに戻すため.html(original)を入れておく
      $sub_category_2.html(originalSubCategory2).find('option').each(function () {
        var dataValSubCategory2 = $(this).data('val'); //data-valの値を取得
        //valueと異なるdata-valを持つ要素を削除
        if (valSubCategory != dataValSubCategory2) {
          $(this).not(':first-child').remove();
        }
      });

      $.each(condition_sub_category, function (index, val) {
        //削除された要素をもとに戻すため.html(original)を入れておく
        val.element.html(val.original).find('option').each(function () {

          var dataValSubCategory2 = $(this).data('val'); //data-valの値を取得
          //valueと異なるdata-valを持つ要素を削除
          if (valSubCategory != dataValSubCategory2) {
            $(this).not(':first-child').remove();
          }

        });
      });

      $.each(condition_sub_category_2, function (index, val) {
        //削除された要素をもとに戻すため.html(original)を入れておく
        val.element.html(val.original).find('option').each(function () {

          var dataVal = $(this).data('val'); //data-valの値を取得
          //valueと異なるdata-valを持つ要素を削除
          if (valSubCategory2 != dataVal) {
            $(this).not(':first-child').remove();
          }

        });
      });

      //サブカテゴリのselect要素が未選択の場合、それより下のselectをdisabledにする
      if ($(this).val() == "") {
        $sub_category_2.attr('disabled', 'disabled');
      } else {
        $sub_category_2.removeAttr('disabled');
      }
      $.each(condition_sub_category, function (index, val) {
        val.element.attr('disabled', 'disabled');
      });
      $.each(condition_sub_category_2, function (index, val) {
        val.element.attr('disabled', 'disabled');
      });
    });


    //サブカテゴリ2のselect要素が変更になるとイベントが発生
    $('.sub_category_2').change(function () {

      //選択されたサブカテゴリ、サブカテゴリ２のvalueを取得し変数に入れる
      var valSubCategory = $('.sub_category').val();
      var valSubCategory2 = $('.sub_category_2').val();

      $.each(condition_sub_category, function (index, val) {
        //削除された要素をもとに戻すため.html(original)を入れておく
        val.element.html(val.original).find('option').each(function () {

          var dataValSubCategory2 = $(this).data('val'); //data-valの値を取得
          //valueと異なるdata-valを持つ要素を削除
          if (valSubCategory != dataValSubCategory2) {
            $(this).not(':first-child').remove();
          }

        });
      });

      $.each(condition_sub_category_2, function (index, val) {
        //削除された要素をもとに戻すため.html(original)を入れておく
        val.element.html(val.original).find('option').each(function () {

          var dataVal = $(this).data('val'); //data-valの値を取得
          //valueと異なるdata-valを持つ要素を削除
          if (valSubCategory2 != dataVal) {
            $(this).not(':first-child').remove();
          }

        });
      });

      //サブカテゴリまたはサブカテゴリ2のselect要素が未選択の場合、それより下の要素をdisabledにする
      if ($('.sub_category').val() == "" || $('.sub_category_2').val() == "") {
        $.each(condition_sub_category, function (index, val) {
          val.element.attr('disabled', 'disabled');
        });
        $.each(condition_sub_category_2, function (index, val) {
          val.element.attr('disabled', 'disabled');
        });
      } else {
        $fit.removeAttr('disabled');
        $design.removeAttr('disabled');

        $.each(condition_sub_category_2, function (index, val) {
          val.element.attr('disabled', 'disabled');
        });

        if ($('.sub_category').val() == "トップス") {
          if ($('.sub_category_2').val() == "カットソー") {
            $neck.removeAttr('disabled');
          } else if ($('.sub_category_2').val() == "シャツ・ブラウス") {
            $coller.removeAttr('disabled');
          } else if ($('.sub_category_2').val() == "パーカー") {
            $zipbutton.removeAttr('disabled');
          }
        } else if ($('.sub_category').val() == "パンツ") {
          $length.removeAttr('disabled');
          $leg.removeAttr('disabled');
          if ($('.sub_category_2').val() == "デニムパンツ") {
            $effect.removeAttr('disabled');
          }
        } else if ($('.sub_category').val() == "スカート") {
          $skirt_length.removeAttr('disabled');
        } else if ($('.sub_category').val() == "ワンピース") {
          $skirt_length.removeAttr('disabled');
        }
      }
    }
    );

    function init() {
      $('.main_category').val("");
      $('.sub_category').val("");
      $('.sub_category_2').val("");
      $('.fit').val("");
      $('.design').val("");
      $('.coller').val("");
      $('.zipbutton').val("");
      $('.length').val("");
      $('.skirt_length').val("");
      $('.leg').val("");
      $('.effect').val("");

      $('.sub_category').attr('disabled', 'disabled');
      $('.sub_category_2').attr('disabled', 'disabled');
      $('.fit').attr('disabled', 'disabled');
      $('.design').attr('disabled', 'disabled');
      $('.coller').attr('disabled', 'disabled');
      $('.zipbutton').attr('disabled', 'disabled');
      $('.length').attr('disabled', 'disabled');
      $('.skirt_length').attr('disabled', 'disabled');
      $('.leg').attr('disabled', 'disabled');
      $('.effect').attr('disabled', 'disabled');
    }
  });

  $('#generator').submit(function () {
    $.ajax({
      'url': '/generator/index',
      'type': 'POST',
      'data': {
        'main_category': $('.main_category').val(),
        'sub_category': $('.sub_category').val(),
        'sub_category_2': $('.sub_category_2').val(),
        'fit': $('.fit').val(),
        'design': $('.design').val(),
        'neck': $('.neck').val(),
        'coller': $('.coller').val(),
        'zipbutton': $('.zipbutton').val(),
        'length': $('.length').val(),
        'skirt_length': $('.skirt_length').val(),
        'leg': $('.leg').val(),
        'effect': $('.effect').val(),
      },
      'success': function (response) {
        $('#descriptionTextarea').val(response)
      },
    });
    return false;
  });