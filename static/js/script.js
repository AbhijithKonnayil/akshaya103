function checkDate()
	{
	alert("Select Date");
	}

function displayDate()
	{	
		var day,month,year;
		var date = new Date();
		switch(date.getDay())
		{
			case 0 : day="Sunday";
					break;
			case 1 : day="Monday";
					break;
			case 2 : day="Tuesday";
					break;
			case 3 : day="Wednesday";
					break;
			case 4 : day="Thrusday";
					break;
			case 5 : day="Friday";
					break;
			case 6 : day="Saturday";
					break;
		}

		switch(date.getMonth())
		{
			case 0 : month="January";
					break;
			case 1 : month="February";
					break;
			case 2 : month="March";
					break;
			case 3 : month="April";
					break;
			case 4 : month="May";
					break;
			case 5 : month="June";
					break;
			case 6 : month="July";
					break;
			case 7 : month="August";
					break;
			case 8 : month="September";
					break;
			case 9 : month="October";
					break;
			case 10 : month="November";
					break;
			case 11 : month="December";
					break;
		}

		document.getElementById('date').innerHTML=(month+" "+ date.getDate() +"," +date.getFullYear()+ "<br>"+ day  );
	}

function myFunction()
{   

    var js_selected_reciept = document.getElementById('{{form.reciept.id_for_label}}').options[document.getElementById('{{form.reciept.id_for_label}}').selectedIndex].text;
    var js_reciept_title = [""];
    var js_reciept_service_fees = [""];
    var js_reciept_ass_bank_acc = [""];
    var js_reciept_ass_fees = [""];
    var js_reciept_id

    {% for r in recieptDetail %}

        js_reciept_title.push('{{r.reciept_title}}');
        js_reciept_service_fees.push({{r.service_fees}});
        js_reciept_ass_bank_acc.push('{{r.ass_bank_acc}}');
        js_reciept_ass_fees.push({{r.ass_fees}});
   
    {% endfor %} 
    var js_bank_list =[""]
    var js_bank_id_list=[""]
    {% for s in bankDetails %}
        js_bank_list.push('{{s.bank_name}}')
        js_bank_id_list.push('{{s.id}}')
    {% endfor %}

    var i;
    for(i=1;i<=js_reciept_title.length;i++)
    {
        if(js_selected_reciept == js_reciept_title[i])
        {   
            
            if(js_reciept_ass_bank_acc[i] == 'None')
            {
            document.getElementById('hide_bank').style.display='none';
            document.getElementById('hide_payment').style.display='none';
            }
            else
            {
            document.getElementById('hide_bank').style.display='inline-table';
            document.getElementById('hide_payment').style.display='inline-table';

            }
            
            document.getElementById('{{form.service_fees.id_for_label}}').value = js_reciept_service_fees[i];
            document.getElementById('{{form.payment_fees.id_for_label}}').value = js_reciept_ass_fees[i];  
            
            document.getElementById('{{form.bank_acc.id_for_label}}').value=js_bank_id_list[js_bank_list.indexOf(js_reciept_ass_bank_acc[i])];
        }
    }
}

function findTotal()
{

	var x = parseFloat(document.getElementById('{{form.payment_fees.id_for_label}}').value);	
	var y = parseFloat(document.getElementById('{{form.service_fees.id_for_label}}').value);
    document.getElementById('form_total').innerHTML = "Rs. " + (x+y) ;
    alert("skdj");
    return x+y;
}

function creditField()
{ 
    if(document.getElementById('{{form.service_on_credit.id_for_label}}').checked==true)
    {
        document.getElementById('amount_paid').style.display='inline-table';
        document.getElementById('{{form.rec_amount.id_for_label}}').value=0;
    }
    else
   {    
        document.getElementById('{{form.rec_amount.id_for_label}}').value=findTotal();
        document.getElementById('amount_paid').style.display='none';     
   }
}

function creditValidation()
{
   var total = findTotal();
   var collected = document.getElementById('{{form.rec_amount.id_for_label}}').value;
    if( collected > total)
    {   
        var balance = collected - total;
        alert("Rs " + balance + "greater" );
        document.getElementById('{{form.rec_amount.id_for_label}}').value=total;
    }
}

