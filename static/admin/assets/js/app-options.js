$(document).ready(function(){

    $('body').on('click', '#open-close', function(){
        $(this).parent().toggleClass('open');
    });

    $('body').on('change', '#fixed-header', function(){
        if ($(this).is(':checked')) {
            $('body').addClass('navbar-fixed')
        } else {
            $('body').removeClass('navbar-fixed')
        }
    });

    $('body').on('change', '#sidebar-navigation', function(){
        if ($(this).is(':checked')) {
            $('body').addClass('sidebar-nav').removeClass('top-nav');
            $('#hidden-sidebar').attr('checked', false);
            $('#top-navigation').attr('checked', false);
        } else {
            $('body').removeClass('sidebar-nav')
        }
    });

    $('body').on('change', '#fixed-navigation', function(){
        if ($(this).is(':checked')) {
            $('body').addClass('fixed-nav')
        } else {
            $('body').removeClass('fixed-nav')
        }
    });

    $('body').on('change', '#compact-sidebar', function(){
        if ($(this).is(':checked')) {
            $('body').addClass('compact-nav');
        } else {
            $('body').removeClass('compact-nav')
        }
    });

    $('body').on('change', '#hidden-sidebar', function(){
        if ($(this).is(':checked')) {
            $('body').removeClass('compact-nav').removeClass('sidebar-nav').removeClass('top-nav')
            $('#sidebar-navigation').attr('checked', false);
            $('#top-navigation').attr('checked', false);
        } else {

        }
    });

    $('body').on('change', '#top-navigation', function(){
        if ($(this).is(':checked')) {
            $('body').addClass('top-nav').removeClass('sidebar-nav');
            $('#hidden-sidebar').attr('checked', false);
            $('#sidebar-navigation').attr('checked', false);
            $('#compact-sidebar').attr('checked', false);
        } else {
            $('body').removeClass('top-nav')
        }
    });

    //colours

    $('body').on('change', '#header-style', function(){
        if (!$(this).is(':checked')) {
            $('header').addClass('navbar-light').removeClass('navbar-dark');
        } else {
            $('header').addClass('navbar-dark').removeClass('navbar-light');
        }
    });

    $('body').on('change', '#brand-style', function(){
        if (!$(this).is(':checked')) {
            $('header').addClass('brand-light').removeClass('brand-dark');
        } else {
            $('header').addClass('brand-dark').removeClass('brand-light');
        }
    });

    $('body').on('change', '#navigation-style', function(){
        if (!$(this).is(':checked')) {
            $('#navigation').addClass('nav-light').removeClass('nav-dark');
        } else {
            $('#navigation').addClass('nav-dark').removeClass('nav-light');
        }
    });

})
/**=========================================================
 * Module: datepicker,js
 * DateTime Picker init
 =========================================================*/

(function($, window, document){

  $(function(){

    if ( ! $.fn.dataTable ) return;

    //
    // Zero configuration
    //

    $('#datatable1').dataTable({
        'paging':   true,  // Table pagination
        'ordering': true,  // Column ordering
        'info':     true,  // Bottom left status text
        // Text translation options
        // Note the required keywords between underscores (e.g _MENU_)
        oLanguage: {
            sSearch:      'Search all columns:',
            sLengthMenu:  '_MENU_ records per page',
            info:         'Showing page _PAGE_ of _PAGES_',
            zeroRecords:  'Nothing found - sorry',
            infoEmpty:    'No records available',
            infoFiltered: '(filtered from _MAX_ total records)'
        }
    });


    //
    // Filtering by Columns
    //

    var dtInstance2 = $('#datatable2').dataTable({
        'paging':   true,  // Table pagination
        'ordering': true,  // Column ordering
        'info':     true,  // Bottom left status text
        // Text translation options
        // Note the required keywords between underscores (e.g _MENU_)
        oLanguage: {
            sSearch:      'Search all columns:',
            sLengthMenu:  '_MENU_ records per page',
            info:         'Showing page _PAGE_ of _PAGES_',
            zeroRecords:  'Nothing found - sorry',
            infoEmpty:    'No records available',
            infoFiltered: '(filtered from _MAX_ total records)'
        }
    });
    var inputSearchClass = 'datatable_input_col_search';
    var columnInputs = $('tfoot .'+inputSearchClass);

    // On input keyup trigger filtering
    columnInputs
      .keyup(function () {
          dtInstance2.fnFilter(this.value, columnInputs.index(this));
      });


    //
    // Column Visibilty Extension
    //

    var dtInstance3 = $('#datatable3').dataTable({
        'paging':   true,  // Table pagination
        'ordering': true,  // Column ordering
        'info':     true,  // Bottom left status text
        // Text translation options
        // Note the required keywords between underscores (e.g _MENU_)
        oLanguage: {
            sSearch:      'Search all columns:',
            sLengthMenu:  '_MENU_ records per page',
            info:         'Showing page _PAGE_ of _PAGES_',
            zeroRecords:  'Nothing found - sorry',
            infoEmpty:    'No records available',
            infoFiltered: '(filtered from _MAX_ total records)'
        },
        sDom:      'C<"clear">lfrtip',
        colVis: {
            order: "alfa",
            "buttonText": "Show/Hide Columns"
        }
    });


  });

}(jQuery, window, document));

/**=========================================================
 * Module: datepicker,js
 * DateTime Picker init
 =========================================================*/

(function($, window, document){

    var Selector = '.datetimepicker';

    $(Selector).each(function() {

      var $this = $(this),
          options = $this.data(); // allow to set options via data-* attributes

      $this.datetimepicker($.extend(
        options,
        { // support for FontAwesome icons
          icons: {
              time:   "fa fa-clock-o",
              date:   "fa fa-calendar",
              up:     "fa fa-arrow-up",
              down:   "fa fa-arrow-down"
          }
        }));

      // Force a dropdown hide when click out of the input
      $(document).on('click', function(){
        $this.data("DateTimePicker").hide();
      });

    });

}(jQuery, window, document));
