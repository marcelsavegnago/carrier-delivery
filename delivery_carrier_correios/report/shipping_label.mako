## -*- coding: utf-8 -*-
<html>
<head>
     <style type="text/css">
        ${css}

.list_main_table {
border:thin solid #E3E4EA;
text-align:center;
border-collapse: collapse;
}
table.list_main_table {
    margin-top: 20px;
}
.list_main_headers {
    padding: 0;
}
.list_main_headers th {
    border: thin solid #000000;
    padding-right:3px;
    padding-left:3px;
    background-color: #EEEEEE;
    text-align:center;
    font-size:12;
    font-weight:bold;
}
.list_main_table td {
    padding-right:3px;
    padding-left:3px;
    padding-top:3px;
    padding-bottom:3px;
}
.list_main_lines,
.list_main_footers {
    padding: 0;
}
.list_main_footers {
    padding-top: 15px;
}
.list_main_lines td,
.list_main_footers td,
.list_main_footers th {
    text-align:left;
    font-size:12;
}

.list_main_lines td {
    border-bottom:thin solid #EEEEEE
}

.list_main_footers td {
    border: thin solid  #ffffff;
}

.list_main_footers th {
    text-align:right;
}

td .total_empty_cell {
    width: 77%;
}
td .total_sum_cell {
    width: 13%;
}

tfoot.totals tr:first-child td{
    padding-top: 15px;
}

.nobreak {
    page-break-inside: avoid;
}
caption.formatted_note {
    text-align:left;
    border-right:thin solid #EEEEEE;
    border-left:thin solid #EEEEEE;
    border-top:thin solid #EEEEEE;
    padding-left:10px;
    font-size:11;
    caption-side: bottom;
}
caption.formatted_note p {
    margin: 0;
}
.list_bank_table {
    text-align:center;
    border-collapse: collapse;
    page-break-inside: avoid;
    display:table;
}

.act_as_row {
   display:table-row;
}
.list_bank_table .act_as_thead {
    background-color: #EEEEEE;
    text-align:left;
    font-size:12;
    font-weight:bold;
    padding-right:3px;
    padding-left:3px;
    white-space:nowrap;
    background-clip:border-box;
    display:table-cell;
}
.list_bank_table .act_as_cell {
    text-align:left;
    font-size:12;
    padding-right:3px;
    padding-left:3px;
    padding-top:3px;
    padding-bottom:3px;
    white-space:nowrap;
    display:table-cell;
}


.list_tax_table {
}
.list_tax_table td {
    text-align:left;
    font-size:12;
}
.list_tax_table th {
}
.list_tax_table thead {
    display:table-header-group;
}


.list_total_table {
    border:thin solid #E3E4EA;
    text-align:center;
    border-collapse: collapse;
}
.list_total_table td {
    border-top : thin solid #EEEEEE;
    text-align:left;
    font-size:12;
    padding-right:3px;
    padding-left:3px;
    padding-top:3px;
    padding-bottom:3px;
}
.list_total_table th {
    background-color: #EEEEEE;
    border: thin solid #000000;
    text-align:center;
    font-size:12;
    font-weight:bold;
    padding-right:3px
    padding-left:3px
}
.list_total_table thead {
    display:table-header-group;
}

.right_table {
    right: 4cm;
    width:"100%";
}

.std_text {
    font-size:12;
}


td.amount, th.amount {
    text-align: right;
    white-space: nowrap;
}

td.date {
    white-space: nowrap;
    width: 90px;
}

td.vat {
    white-space: nowrap;
}
.address .recipient {
    font-size: 12px;
    margin-left: 350px;
    margin-right: 120px;
    float: right;
}

.main_col1 {
    width: 40%;
}
td.main_col1 {
    text-align:left;
    vertical-align:top;
}
.main_col2 {
    width: 10%;
    vertical-align:top;
}
.main_col3 {
    width: 10%;
    text-align:center;
    vertical-align:top;
}
.main_col6 {
    width: 10%;
    vertical-align:top;
}
.main_col4 {
	width: 10%;
	text-align:right;
    vertical-align:top;
}
.main_col5 {
    width: 7%;
    text-align:left;
    vertical-align:top;
}
.main_col7 {
    width: 13%;
    vertical-align:top;
}

    </style>

</head>
<body>
    %for label in objects:
        <table style="border:1px solid black;">
            <tbody>
            <tr>
                <th>
                    %if label.x_barcode_id.image:
                        <img src='data:image/png;base64,${label.x_barcode_id.image}'/>
                    %else:
                        &nbsp;
                    %endif
                </th>
            </tr>
            <tr>
                <td>
                    <table>
                        <tbody>
                        <tr>
                            <td>
                                <table style="border-style: none; white-space: nowrap;">
                                    <tbody>
                                    <tr>
                                        <td>${ label.name }</td>
                                    </tr>
                                    <tr>
                                        <td>
                                            Destinat&aacute;rio: ${label.partner_id.legal_name}</td>
                                    </tr>
                                    <tr>
                                        <td>Rua: ${label.partner_id.street}
                                            , ${label.partner_id.number}
                                            , ${label.partner_id.street2 or ''}
                                            </td>
                                    </tr>
                                    <tr>
                                        <td>Complemento: ${label.partner_id.street2 or ''}
                                        </td>
                                    </tr>
                                    <tr>
                                        <td>
                                            Bairro: ${label.partner_id.district}</td>
                                    </tr>
                                    <tr>
                                        <td>
                                            CEP:&nbsp;${label.partner_id.zip}&nbsp;&nbsp;</td>
                                    </tr>
                                    <tr>
                                        <td>
                                            Cidade: ${label.partner_id.l10n_br_city_id.name}
                                            , ${label.partner_id.l10n_br_city_id.state_id.code}</td>
                                    </tr>
                                    </tbody>
                                </table>
                            </td>
                        </tr>
                        </tbody>
                    </table>
                </td>
            </tr>

            <tr>
                <td>
                    <table align="left" style="border-style:none; white-space: nowrap;">
                        <tbody>
                        <tr>
                            <td><span style="font-size:8px;">
                                Remetente: ${company.street}
                                - ${company.number} - ${company.district}
                                - ${company.street2 or ''}
                                - ${company.zip}
                                - ${company.l10n_br_city_id.name}
                                (${company.partner_id.l10n_br_city_id.state_id.code})</span>
                            </td>
                        </tr>
                        </tbody>
                    </table>

                    <p>&nbsp;</p>
                </td>
            </tr>
            </tbody>
        </table>

    %endfor
</body>
</html>