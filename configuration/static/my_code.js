$(document).ready(function(){
    show_hide();
    $('#id_type').change(function(){
        show_hide();
    });
    function show_hide(){
        if ($("#id_type").val() == 'aM' ){
                $(".module")[1].style.display="block"
            }
        else{
             $(".module")[1].style.display="none"
        }
    }
});

//
// $(document).ready(function(){
//     show_hide();
//     $('#id_type').change(function(){
//         show_hide();
//     });
//     function show_hide(){
//         if ($("#id_type").val() == 'aD' ){
//                 $(".form-row.field-is_key").show();
//                 $(".form-row.field-unit").show();
//             }
//         else{
//               $(".form-row.field-is_key").hide();
//               $(".form-row.field-unit").hide();
//         }
//     }
// });



// $(document).ready(function(){
//     show_hide();
//     $('#id_type').change(function(){
//         show_hide();
//     });
//     function show_hide(){
//         if ($("#id_type").val() == 'aD'){
//                 $("#id_is_key").style.display="block";
//                 $("#id_unit").style.display = "block";
//             }
//         else{
//                 $("#id_is_key").style.display="none";
//                 $(".form-row.field-name").style.display = "none";
//         }
//     }
// });