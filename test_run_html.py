html = '''<html xmlns="http://www.w3.org/1999/xhtml"><head><title>

</title><link href="css/innerother.css" rel="stylesheet" type="text/css"><link href="css/cssverticalmenu.css" rel="stylesheet" type="text/css">
    <script type="text/javascript" src="js/cssverticalmenu.js"></script>
    <script type="text/javascript" src="lib/jquery-1.4.2.min.js"></script>
    <script type="text/javascript" src="lib/jquery.jcarousel.js"></script>
    <script src="SpryAssets/SpryValidationTextField.js" type="text/javascript"></script>
    <link rel="stylesheet" type="text/css" href="skins/tango/skin.css"><link href="SpryAssets/SpryValidationTextField.css" rel="stylesheet" type="text/css">
    <style type="text/css">
        .modalBackground {
            background-color: Gray;
            filter: alpha(opacity=80);
            opacity: 0.8;
            z-index: 10000;
        }

        table {
            margin: 0px auto;
            padding: 0;
            font-size: 0.9em;
            color: #444;
        }

            table.rounded-corners tr:first-child td:first-child {
                border-top-left-radius: 5px;
            }

            table.rounded-corners tr:first-child td:last-child {
                border-top-right-radius: 5px;
            }

            table.rounded-corners tr:last-child td:first-child {
                border-bottom-left-radius: 5px;
            }

            table.rounded-corners tr:last-child td:last-child {
                border-bottom-right-radius: 5px;
            }

            table.rounded-corners tr td {
                border-top: 1px solid #839c3e;
                border-bottom: 1px solid #839c3e;
                border-left: 1px solid #839c3e;
                border-right: 1px solid #839c3e;
                margin: 11px 0 11px 0;
                padding: 8px 6px;
                background: #fff;
            }

            table.rounded-corners tr:nth-child(even) {
                background: #ECF9D9;
            }

            table.rounded-corners tr:nth-child(odd) {
                background: #fff;
            }

            table.rounded-corners tr:hover td {
                background: #d0e2c8;
            }

            table.rounded-corners thead {
                background-color: #B2D87A;
            }

                table.rounded-corners thead th {
                    background-color: #B2D87A;
                    font-weight: bold;
                }

            table.rounded-corners tbody tr th {
                background-color: #CAE4A3;
                padding: 10px 2px;
                width: -10%;
            }

            table.rounded-corners tbody tr td span {
                padding: 5px 10px;
            }

            table.rounded-corners tbody tr td a {
                padding: 5px 10px;
                color: #485c05;
            }

            table tr td {
                padding: 8px 0px;
            }

        .radiobutton {
            float: right;
            margin: 10px 0;
            width: 70%;
        }

            .radiobutton input[type="radio"] {
                float: left;
            }

            .radiobutton label {
                text-align: right;
                margin: -13px 12px 0px 10px;
                float: left;
                padding: 0px;
            }

        .button {
            background: #485C05;
            color: #fff;
            border: 1px solid #485C05;
            padding: 6px 12px;
            border-radius: 5px;
            font-size: 1.2em;
        }

        fieldset {
            border: 1px solid #839c3e;
            border-radius: 5px;
            background: #E7F6E1;
            width: 88%;
            margin: 0 auto;
            letter-spacing: 1px;
        }

        legend {
            padding: 5px 20px;
            margin: 0 auto !important;
            text-transform: capitalize;
            font-weight: bold;
        }
    </style>
</head>

<body>
    <form name="form1" method="post" action="livestockcensus.aspx" id="form1">
<div>
<input type="hidden" name="__EVENTTARGET" id="__EVENTTARGET" value="">
<input type="hidden" name="__EVENTARGUMENT" id="__EVENTARGUMENT" value="">
<input type="hidden" name="__LASTFOCUS" id="__LASTFOCUS" value="">
<input type="hidden" name="__VIEWSTATE" id="__VIEWSTATE" value="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">
</div>

<script type="text/javascript">
//<![CDATA[
var theForm = document.forms['form1'];
if (!theForm) {
    theForm = document.form1;
}
function __doPostBack(eventTarget, eventArgument) {
    if (!theForm.onsubmit || (theForm.onsubmit() != false)) {
        theForm.__EVENTTARGET.value = eventTarget;
        theForm.__EVENTARGUMENT.value = eventArgument;
        theForm.submit();
    }
}
//]]>
</script>


<div>

	<input type="hidden" name="__VIEWSTATEENCRYPTED" id="__VIEWSTATEENCRYPTED" value="">
</div>

        <div id="main">
            <div id="accessibility_pan">
                .<ul>
                    <li><a href="#skip" title="Skip to Main Content">Skip to Main Content</a></li>
                    <li><a href="screenreaderaccess.html" title="Screen Reader Access" target="_self">Screen
                    Reader Access</a></li>
                    <li class="img"><a href="#" title="Decrease Text">
                        <img src="imagedefault/a_decrease.png" width="20" height="16" border="0" alt="Decrease Text"></a></li>
                    <li class="pic"><a href="#" title="Normal Text">
                        <img src="imagedefault/normal_icon.png" width="20" height="16" border="0" alt="Normal Text"></a></li>
                    <li><a href="#" title="Increase Text">
                        <img src="imagedefault/a_increase.png" width="20" height="16" border="0" alt="Increase Text"></a></li>
                    <li class="img"><a href="indexcontrast.html" title="High Contrast" target="_self">
                        <img src="imagedefault/highcontrast.png" width="20" height="16" border="0" alt="High Contrast"></a></li>
                    <li><a href="#" title="Normal contrast">
                        <img src="imagedefault/normal_icon.png" width="20" height="16" border="0" alt="Normal contrast"></a></li>
                    <li><a href="index.html" title="Green Theme" target="_self">
                        <img src="imagedefault/green.png" width="20" height="16" border="0" alt="Green Theme"></a></li>
                    <li><a href="indexblue.html" title="Blue Theme" target="_self">
                        <img src="imagedefault/blue.png" width="20" height="16" border="0" alt="Blue Theme"></a></li>
                    <li><a href="indexbrown.html" title="Brown Theme" target="_self">
                        <img src="imagedefault/brown.png" width="20" height="16" border="0" alt="Brown Theme"></a></li>
                    <li><a href="#" title="This Website in Hindi (External website that opens in a new window)">????? ???</a></li>
                </ul>
            </div>
            <div class="clear">
            </div>
            <div id="headertop">
                <div id="header">
                    <div class="title">
                        <a href="../FarmerHome.aspx" title="Farmer Portal, Ministry of Agriculture,Government of India">
                            <img src="imagedefault/title.png" width="513" height="79" alt="Farmer Portal, Ministry of Agriculture,Government of India" border="0"></a>
                        <br>
                        <img alt="Farmer Portal" src="imagedefault/beta.png">
                    </div>
                </div>
            </div>
            <div class="clear">
            </div>
            <div id="menu">
                <a id="skip" name="skip"></a>
                <ul>
                    <li><a href="#" title="Market Price">Market Price</a>
                        <ul>
                            <li><a href="marketprice.html" title="Other Agri Commodities" target="_self">Other Agri
                            Commodities </a></li>
                            <li><a href="http://www.trifed.in/trifed/(S(pfgb3bhr5lla4itmhzu1k2xx))/present_status.aspx" title="Minor Forest Produce" target="_blank" class="reglanguage">Minor Forest Produce</a></li>
                        </ul>
                    </li>
                    <li><a href="#" title="Storage">Storage</a>
                        <ul>
                            <li><a href="CWC_Link.aspx" title="CWC">CWC</a></li>
                            <li><a href="SWC_Link.aspx" title="SWC">SWC</a></li>
                            <li><a href="NHM_Link.aspx" title="NHM">NHM</a></li>
                            <li><a href="NHB_Link.aspx" title="NHB">NHB</a></li>
                            <li><a href="COLD_STROAGE_Link.aspx" title="Cold Stores">Cold Stores </a></li>
                            <li><a href="NABARD_Link.aspx" title="Grameen Bhandaran">Grameen Bhandaran</a></li>
                            <li><a href="MPEDA_Link.aspx" title="MPEDA">MPEDA</a></li>
                        </ul>
                    </li>
                    <li><a href="#" title="Insurance / Credit">Insurance / Credit</a>
                        <ul>
                            <li><a href="insurance.html" title="Insurance" target="_self">Insurance</a> </li>
                            <li><a href="#" title="Credit">Credit</a>
                                <ul>
                                    <li><a href="http://dbie.rbi.org.in/InfoViewApp/MOFSelectParam.jsp" title="Branch Locator" target="_blank">Branch Locator</a></li>
                                    <li><a href="debitrelief.html" title="Debt Relief" target="_self">Debt Relief </a>
                                    </li>
                                    <li><a href="shortloan.html" title="Short Term Credit" target="_self">Short Term Credit</a></li>
                                    <li><a href="midlongloan.html" title="Medium/Long Term Loans" target="_self">Med./Long
                                    Term Loans </a></li>
                                    <li><a href="bank.html" title="Agricultural Banking" target="_self">Agricultural Banking
                                    </a></li>
                                    <li><a href="agriculturecredit.html" title="Agricultural Credit" target="_self">Agricultural
                                    Credit </a></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li><a href="#" title="Crops" target="_self">Crops</a>
                        <ul>
                            <li><a href="#" title="Wheat" target="_self">Wheat</a>
                                <ul>
                                    <li><a href="cropstaticswheat.html" title="General Info Wheat" target="_self">General
                                    Info</a></li>
                                    <li><a href="http://ppqs.gov.in/pack/ipmpackage/wheat.pdf" title="Pest &amp; Diseases" target="_blank">Pest &amp; Diseases</a></li>
                                    <li><a href="http://smis.dacnet.nic.in/%28S%28s54q5qz3lgayuzmh3g2yfyvp%29%29/Report/crvVarietyList.aspx?code=A0104" title="Seed Varieties" target="_blank">Seed Varieties</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="Maize">Maize</a>
                                <ul>
                                    <li><a href="cropstaticsmaize.html" title="General Info Maize" target="_self">General
                                    Info</a></li>
                                    <li><a href="http://ppqs.gov.in/pack/ipmpackage/maize.pdf" title="Pest &amp; Diseases" target="_blank">Pest &amp; Diseases</a></li>
                                    <li><a href="http://smis.dacnet.nic.in/%28S%28s2ir4hsps1nvrmjihfwbi1hz%29%29/report/crvvarietyList.aspx?code=A0207" title="Seed Varieties" target="_blank">Seed Varieties</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="Rice">Rice</a>
                                <ul>
                                    <li><a href="cropstaticsrice.html" title="General Info Rice" target="_self">General
                                    Info</a></li>
                                    <li><a href="http://ppqs.gov.in/pack/ipmpackage/rice.pdf" title="Pest &amp; Diseases" target="_blank">Pest &amp; Diseases</a></li>
                                    <li><a href="http://smis.dacnet.nic.in/%28S%281pwga0pui21xmclq0joyqxcz%29%29/Report/crvVarietyList.aspx?code=A0102" title="Seed Varieties" target="_blank">Seed Varieties</a></li>
                                    <li><a href="http://rkmp.co.in/diagnostic/" title="Diagnostic Tool" target="_blank">Diagnostic Tool</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="Pulses">Pulses</a>
                                <ul>
                                    <li><a href="cropstaticspulses.html" title="General Info Pulses" target="_self">General
                                    Info</a></li>
                                    <li><a href="http://ppqs.gov.in/pack/ipmpackage/gram.pdf" title="Pest &amp; Diseases" target="_blank">Pest &amp; Diseases</a></li>
                                    <li><a href="http://smis.dacnet.nic.in/%28S%28sl04mcjsphwj2pjcc53auyws%29%29/Report/crvVarietyList.aspx?code=A03" title="Seed Varieties" target="_blank">Seed Varieties</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="Jute">Jute</a>
                                <ul>
                                    <li><a href="cropstaticsjute.html" title="General Info Jute" target="_self">General
                                    Info</a></li>
                                    <li><a href="pestanddiseasjute.html" title="Pest &amp; Diseases" target="_blank">Pest
                                    &amp; Diseases</a></li>
                                    <li><a href="http://smis.dacnet.nic.in/%28S%28s54q5qz3lgayuzmh3g2yfyvp%29%29/Report/crvVarietyList.aspx?code=A0502" title="Seed Varieties" target="_blank">Seed Varieties</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="Sugarcane">Sugarcane</a>
                                <ul>
                                    <li><a href="cropstaticssugarcane.html" title="General Info Sugarcane" target="_self">General Info</a></li>
                                    <li><a href="http://ppqs.gov.in/pack/ipmpackage/sugar.pdf" title="Pest &amp; Diseases" target="_blank">Pest &amp; Diseases</a></li>
                                    <li><a href="http://smis.dacnet.nic.in/%28S%28s54q5qz3lgayuzmh3g2yfyvp%29%29/Report/crvVarietyList.aspx?code=A0701" title="Seed Varieties" target="_blank">Seed Varieties</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="Other Crops">Other Crops</a>
                                <ul>
                                    <li><a href="IPMPackageofPractices.html" title="Pest &amp; Diseases" target="_self">Pest &amp; Diseases</a></li>
                                    <!--<li><a href="http://smis.dacnet.nic.in/%28S%28eevbzoaxg033cmtja3clol2t%29%29/report/centralvariety.aspx">Seed Varieties</a></li>-->
                                    <!--<li><a href="#" title="Crop Facts" target="_blank">Crop Facts</a></li>-->
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li><a href="#" title="Extension Activities">Extension Activities</a>
                        <ul>
                            <li>
                                <a onclick="window.document.forms[0].target='_blank';" id="lnkDemonstrations" href="javascript:__doPostBack('lnkDemonstrations','')">Demonstrations</a>
                            </li>
                            <li>
                                <a onclick="window.document.forms[0].target='_blank';" id="lnkFarmerFriend" href="javascript:__doPostBack('lnkFarmerFriend','')">Farmer Friend</a>
                            </li>
                            <li>
                                <a onclick="window.document.forms[0].target='_blank';" id="lnkFarmSchool" href="javascript:__doPostBack('lnkFarmSchool','')">Farm School</a>
                            </li>
                        </ul>
                    </li>
                    <li><a href="#" title="Beneficiary List">Beneficiary List</a>
                        <ul>
                            <li><a href="http://midhwf.nic.in/Masters/Dash.aspx" title="NHM" target="_blank">NHM</a></li>
                            <li><a href="http://nfsm.gov.in/nfmis/rpt/total_beneficiaryCount.aspx" title="NFSM" target="_blank">NFSM</a></li>
                        </ul>
                    </li>
                    <li><a href="#" title="MSP">MSP</a>
                        <ul>
                            <li><a href="mspdet.html" target="_self" title="MSP Determination">MSP Determination</a></li>
                            <li><a href="http://cacp.dacnet.nic.in/" target="_blank" title="Questionnaire">Questionnaire</a>
                                <ul>
                                    <li><a href="http://cacp.dacnet.nic.in/KeyBullets.aspx?pid=47" target="_blank" title="Kharif">Kharif</a></li>
                                    <li><a href="http://cacp.dacnet.nic.in/KeyBullets.aspx?pid=48" target="_blank" title="Rabi">Rabi</a></li>
                                    <li><a href="http://cacp.dacnet.nic.in/KeyBullets.aspx?pid=49" target="_blank" title="Sugarcane">Sugarcane </a></li>
                                    <li><a href="http://cacp.dacnet.nic.in/KeyBullets.aspx?pid=45" target="_blank" title="Copra">Copra</a></li>
                                    <li><a href="http://cacp.dacnet.nic.in/KeyBullets.aspx?pid=46" target="_blank" title="Jute">Jute</a></li>
                                    <li><a href="http://cacp.dacnet.nic.in/KeyBullets.aspx?pid=69" target="_blank" title="Palm Oil">Palm Oil</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="Notified MSP">Notified MSP</a>
                                <ul>
                                    <li><a href="mspstatements.html" target="_self" title="Current">Current</a></li>
                                    <li><a href="http://eands.dacnet.nic.in/MSP.htm" target="_blank" title="Archives">Archives</a></li>
                                </ul>
                            </li>
                        </ul>
                    </li>
                    <li><a href="#" title="Animal Husbandry">Animal Husbandry</a>
                        <ul>
                            <li><a href="http://www.dahd.nic.in/dahd/schemes.aspx" target="_blank" title="Schemes">Schemes</a></li>
                            <li><a href="http://www.dahd.nic.in/dahd/guidelines.aspx" target="_blank" title="Guidelines">Guidelines</a></li>
                            <li><a href="http://www.nadrs.gov.in/SitePages/SMS%20System.aspx" target="_blank" title="Report Disease">Report Disease</a></li>
                        </ul>
                    </li>
                    <li><a href="#" title="Login">Login</a>
                        <ul>
                            <li><a href="NewPagewith.aspx" title="Booklets and Fliers">Booklets and Flyers</a></li>
                            <li><a href="#" title="Agromet">Agromet</a>
                                <ul>
                                    <li>
                                        <a id="lnkAFMU" href="javascript:__doPostBack('lnkAFMU','')">AFMU</a>
                                    </li>
                                    <li>
                                        <a id="lnkMetCenter" href="javascript:__doPostBack('lnkMetCenter','')">Met Center</a>
                                    </li>
                                    <li>
                                        <a id="lnkRegionalCenter" href="javascript:__doPostBack('lnkRegionalCenter','')">Regional Center</a>
                                    </li>
                                    <li>
                                        <a id="lnkIMDHQ" href="javascript:__doPostBack('lnkIMDHQ','')">IMD HQ</a>
                                    </li>
                                </ul>
                            </li>
                            <li><a href="#" title="State">State</a>
                                <ul>
                                    <li><a href="http://smis.dacnet.nic.in/%28S%28rpwindlqgqyywg420vp3cit4%29%29/LoginForm.aspx?farmer=true" title="Seed Dealer">Seed Dealer</a></li>
                                    <li>
                                        <a id="lnkFertilizerState" href="javascript:__doPostBack('lnkFertilizerState','')">Fertilizer Dealer</a>
                                    </li>
                                    <li>
                                        <a id="lnkPesticideState" href="javascript:__doPostBack('lnkPesticideState','')">Pesticide Dealer</a>
                                    </li>
                                    <li>
                                        <a id="lnkPop" href="javascript:__doPostBack('lnkPop','')">POP</a>
                                    </li>
                                    <li><a href="State_Storage_Login.aspx" title="Storage" target="_blank">Storage</a></li>
                                    <li><a href="MSPLogin.aspx" title="MSP" target="_blank">MSP</a></li>
                                </ul>
                            </li>
                            <li><a href="#" title="District">District</a>
                                <ul>
                                    <li><a href="http://smis.dacnet.nic.in/LoginDistrict.aspx?farmer=true" title="Seed Dealer">Seed Dealer</a></li>
                                    <li>
                                        <a id="lnkFertilizerDistrict" href="javascript:__doPostBack('lnkFertilizerDistrict','')">Fertilizer Dealer</a>
                                    </li>
                                    <li>
                                        <a id="lnkPesticideDistrict" href="javascript:__doPostBack('lnkPesticideDistrict','')">Pesticide Dealer</a>
                                    </li>
                                </ul>
                            </li>
                            <li><a href="#" title="Farm Machinery">Farm Machinery</a>
                                <ul>
                                    <li><a href="#" title="Manufacturer/Trader">Manufacturer/Trader</a>
                                        <ul>
                                            
                                            <li>
                                                <a id="lnkNewRegistration" href="javascript:__doPostBack('lnkNewRegistration','')">New Registration</a></li>
                                            
                                            <li>
                                                <a id="lnkRegistered" href="javascript:__doPostBack('lnkRegistered','')">Registered</a></li>
                                        </ul>
                                    </li>
                                    <li><a href="#" title="Authentication Authority">Authentication Authority</a>
                                        <ul>
                                            <li><a href="FarmMechanisation/AssocationLogin.aspx" title="Association &amp; FMTTI ">Association &amp; FMTTI </a></li>
                                            
                                            <li>
                                                <a id="lnkStateApps" href="javascript:__doPostBack('lnkStateApps','')">State</a></li>
                                        </ul>
                                    </li>
                                    <li><a href="FarmMechanisation/LoginDealer.aspx" title="Dealer">Dealer</a></li>
                                    <li><a href="FarmMechanisation/AdminLogin.aspx" title="M &amp; T Division">M &amp; T
                                    Division</a></li>
                                    <li><a href="FarmMechanisation/Publiccorner.aspx" title="Public Corner">Citizen Corner</a></li>
                                </ul>
                            </li>
                            <li><a href="SeedAvailability/Login.aspx" title="Seed Avalibility">Seed Avalibility</a></li>
                            <li><a href="http://farmer.gov.in/recais/login.aspx" title="NeGP-A">NeGP-A</a></li>
                            <li><a href="#" title="Feedback">Feedback</a>
                                <ul>
                                    <li><a href="feedback/FeedbackLogin.aspx" title="Admin">Admin</a></li>
                                    <li><a href="feedback/FeedbackStats.aspx" title="Status">Status</a></li>
                                </ul>
                            </li>
                            <li><a href="DataEntryReport.aspx" title="Data Entry reports">Data Entry Progress</a></li>
                            
                        </ul>
                    </li>
                </ul>
            </div>
            <div class="clear">
            </div>
            <div class="breadcrumb">
                <ul>
                    <li><a href="../FarmerHome.aspx" title="Home Page" target="_self">Home »</a></li>
                    <li>19th LIVESTOCK CENSUS-2012</li>
                </ul>
            </div>
            <div class="clear">
            </div>
            <div id="contentcontainer">
                <div id="middlepnl4">

                    <fieldset>
                        <legend>livestock filter</legend>
                        <table width="80%" align="center">
                            <tbody><tr>
                                <td>Select State</td>
                                <td width="60%">
                                    <select name="ddlstate" onchange="javascript:setTimeout('__doPostBack(\'ddlstate\',\'\')', 0)" id="ddlstate" style="color:#2B3D12;width:340px;">
	<option value="0">--Select State--</option>
	<option value="35">ANDAMAN &amp; NICOBAR ISLANDS</option>
	<option selected="selected" value="28">ANDHRA PRADESH</option>
	<option value="12">ARUNACHAL PRADESH</option>
	<option value="18">ASSAM</option>
	<option value="10">BIHAR</option>
	<option value="04">CHANDIGARH</option>
	<option value="22">CHHATTISGARH</option>
	<option value="26">DADRA &amp; NAGAR HAVELI</option>
	<option value="25">DAMAN &amp; DIU</option>
	<option value="30">GOA</option>
	<option value="24">GUJARAT</option>
	<option value="06">HARYANA</option>
	<option value="02">HIMACHAL PRADESH</option>
	<option value="01">JAMMU &amp; KASHMIR</option>
	<option value="20">JHARKHAND</option>
	<option value="29">KARNATAKA</option>
	<option value="32">KERALA</option>
	<option value="31">LAKSHADWEEP</option>
	<option value="23">MADHYA PRADESH</option>
	<option value="27">MAHARASHTRA</option>
	<option value="14">MANIPUR</option>
	<option value="17">MEGHALAYA</option>
	<option value="15">MIZORAM</option>
	<option value="13">NAGALAND</option>
	<option value="07">NCT OF DELHI</option>
	<option value="21">ODISHA</option>
	<option value="34">PUDUCHERRY</option>
	<option value="03">PUNJAB</option>
	<option value="08">Rajasthan</option>
	<option value="11">SIKKIM</option>
	<option value="33">TAMIL NADU</option>
	<option value="16">TRIPURA</option>
	<option value="09">UTTAR PRADESH</option>
	<option value="05">UTTARAKHAND</option>
	<option value="19">WEST BENGAL</option>

</select>
                                </td>
                            </tr>
                               <tr>
                                <td>Select District</td>
                                <td>
                                    <select name="ddldistrict" onchange="javascript:setTimeout('__doPostBack(\'ddldistrict\',\'\')', 0)" id="ddldistrict" style="color:#2B3D12;width:340px;">
	<option value="0">--Select district--</option>
	<option selected="selected" value="532">Adilabad</option>
	<option value="553">Anantapur</option>
	<option value="554">Chittoor</option>
	<option value="545">East Godavari</option>
	<option value="548">Guntur</option>
	<option value="536">Hyderabad</option>
	<option value="534">Karimnagar</option>
	<option value="541">Khammam</option>
	<option value="547">Krishna</option>
	<option value="552">Kurnool</option>
	<option value="538">Mahbubnagar</option>
	<option value="535">Medak</option>
	<option value="539">Nalgonda</option>
	<option value="533">Nizamabad</option>
	<option value="549">Prakasam</option>
	<option value="537">Rangareddy</option>
	<option value="550">Sri Potti Sriramulu Nellore</option>
	<option value="542">Srikakulam</option>
	<option value="544">Visakhapatnam</option>
	<option value="543">Vizianagaram</option>
	<option value="540">Warangal</option>
	<option value="546">West Godavari</option>
	<option value="551">Y.S.R.</option>

</select>
                                </td>
                            </tr>
                               <tr>
                                <td>Select Tehsil / Block</td>
                                <td>
                                    <select name="ddlblock" id="ddlblock" style="color:#2B3D12;width:340px;">
	<option value="0">--Select Tahsil/Block--</option>
	<option selected="selected" value="04306">Adilabad</option>
	<option value="04319">Asifabad</option>
	<option value="04323">Bazarhathnoor</option>
	<option value="04317">Bejjur</option>
	<option value="04308">Bela</option>
	<option value="04350">Bellampalle</option>
	<option value="04339">Bhainsa</option>
	<option value="04328">Bhimini</option>
	<option value="04324">Boath</option>
	<option value="04356">Chennur</option>
	<option value="04329">Dahegaon</option>
	<option value="04348">Dandepalle</option>
	<option value="04343">Dilawarpur</option>
	<option value="04310">Gudihathnoor</option>
	<option value="04322">Ichoda</option>
	<option value="04311">Inderavelly</option>
	<option value="04307">Jainad</option>
	<option value="04320">Jainoor</option>
	<option value="04355">Jaipur</option>
	<option value="04334">Jannaram</option>
	<option value="04335">Kaddam (Peddur)</option>
	<option value="04318">Kagaznagar</option>
	<option value="04349">Kasipet</option>
	<option value="04313">Kerameri</option>
	<option value="04347">Khanapur</option>
	<option value="04351">Kotapalle</option>
	<option value="04316">Kouthala</option>
	<option value="04338">Kubeer</option>
	<option value="04337">Kuntala</option>
	<option value="04345">Laxmanchanda</option>
	<option value="04342">Lokeswaram</option>
	<option value="04353">Luxettipet</option>
	<option value="04346">Mamda</option>
	<option value="04354">Mancherial</option>
	<option value="04352">Mandamarri</option>
	<option value="04341">Mudhole</option>
	<option value="04312">Narnoor</option>
	<option value="04331">Nennal</option>
	<option value="04325">Neradigonda</option>
	<option value="04344">Nirmal</option>
	<option value="04327">Rebbana</option>
	<option value="04336">Sarangapur</option>
	<option value="04326">Sirpur</option>
	<option value="04315">Sirpur (T)</option>
	<option value="04309">Talamadugu</option>
	<option value="04305">Tamsi</option>
	<option value="04332">Tandur</option>
	<option value="04340">Tanoor</option>
	<option value="04333">Tiryani</option>
	<option value="04321">Utnoor</option>
	<option value="04330">Vemanpalle</option>
	<option value="04314">Wankdi</option>

</select>
                                </td>
                            </tr>
                            <tr>
                                <td>Choose</td>
                                <td class="radiobutton">
                                    <input id="rd_animal" type="radio" name="s" value="rd_animal" checked="checked"><label for="rd_animal">Animal</label>
                                    <input id="rd_bird" type="radio" name="s" value="rd_bird" onclick="javascript:setTimeout('__doPostBack(\'rd_bird\',\'\')', 0)"><label for="rd_bird">Bird</label>
                                </td>
                            </tr>
                            <tr>
                                <td>Animal / Bird Type</td>
                                <td>
                                    <select name="ddlname" onchange="javascript:setTimeout('__doPostBack(\'ddlname\',\'\')', 0)" id="ddlname" style="color:#2B3D12;width:340px;">
	<option value="0">--Select--</option>
	<option value="[19LiveStock_Cattle]">Cattle</option>
	<option selected="selected" value="[19LiveStock_Buffalos]">Buffaloes</option>
	<option value="[19LiveStock_Yaks]">Yaks</option>
	<option value="[19LiveStock_Mithuns]">Mithuns</option>
	<option value="[19LiveStock_Sheep]">Sheep</option>
	<option value="[19LiveStock_Goats]">Goat</option>

</select>
                                </td>
                            </tr>
                            <tr>
                                <td>Household / Non Household</td>
                                <td>
                                    <select name="ddlHouse_non" id="ddlHouse_non" style="color:#2B3D12;width:340px;">
	<option value="0">--Select--</option>
	<option selected="selected" value="H">Households</option>
	<option value="N">Non Household</option>

</select>
                                </td>
                            </tr>
                            <tr>
                                <td>Area</td>
                                <td>
                                    <select name="ddlarea" id="ddlarea" style="color:#2B3D12;width:340px;">
	<option value="0">--Select--</option>
	<option selected="selected" value="R">Rural</option>
	<option value="U">Urban</option>

</select>
                                </td>
                            </tr>
                            <tr>
                                <td>
                                    
                                </td>
                                <td>
                                    
                                </td>
                            </tr>

                            <tr>
                                <td>&nbsp;</td>
                                <td class="radiobutton">
                                    <input type="submit" name="btnfilter" value="Filter" id="btnfilter" style="color:#3A5218;background-color:#C5DDA2;font-size:Medium;font-weight:bold;text-decoration:none;width:111px;">
                                </td>
                            </tr>

                        </tbody></table>
                    </fieldset>
                    
                    

                    
                    

                    <table id="dlist_buffalo" class="rounded-corners" cellspacing="0" border="0" style="width:100%;border-collapse:collapse;">
	<tbody><tr>
		<td>
                            <table style="text-align: center; width: 100%;">
                                <tbody><tr>
                                    <td colspan="15" style="text-align: left;">BUFFALOES</td>
                                </tr>
                                <tr>
                                    <th rowspan="3" width="5%">Address</th>
                                    <th colspan="6" style="background-color: #3A5218; color: #FFFFCC;">Male</th>
                                    <th colspan="7" style="background-color: #3A5218; color: #FFFFCC;">Female</th>
                                    
                                    <th rowspan="3" style="background-color: #3A5218; color: #FFFFCC;" width="10%">TOTAL</th>
                                </tr>
                                <tr>
                                    <th rowspan="2" width="10%">Upto 2 Year</th>
                                    <th colspan="4">Over 2&nbsp; Year</th>
                                    <th rowspan="2" style="background-color: #c5dda2" width="10%">Total Male</th>
                                    <th rowspan="2" width="5%">Under<br>
                                        1 year</th>
                                    <th rowspan="2">1 to 3<br>
                                        years</th>
                                    <th colspan="4">Over 3&nbsp; Year</th>
                                    <th rowspan="2" style="background-color: #c5dda2" width="10%">Total Female</th>

                                </tr>
                                <tr>
                                    <th width="5%">Used for<br>
                                        breeding only </th>
                                    <th width="5%">Used for<br>
                                        draught only</th>
                                    <th width="5%">Used for both<br>
                                        draught and breedin</th>
                                    <th width="5%">Others</th>
                                    <th width="5%">In milk</th>
                                    <th width="5%">Dry</th>
                                    <th width="5%">Not calved once</th>
                                    <th width="5%">Others</th>
                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Jamdapur</td>
                                    <td width="10%">0</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">6</td>
                                    <td width="5%">140</td>
                                    <td width="5%">8</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">156</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">158</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Mallapur</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">2</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Dimma</td>
                                    <td width="10%">0</td>
                                    <td width="5%">5</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">5</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">5</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Pochara</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">2</td>
                                    <td width="5%">1</td>
                                    <td width="5%">174</td>
                                    <td width="5%">8</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">185</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">185</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Tarada (Srimath)</td>
                                    <td width="10%">0</td>
                                    <td width="5%">5</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">5</td>
                                    <td width="5%">14</td>
                                    <td width="5%">5</td>
                                    <td width="5%">38</td>
                                    <td width="5%">20</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">77</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">82</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Rampoor (Royati)</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Bheemseri</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">4</td>
                                    <td width="5%">5</td>
                                    <td width="5%">160</td>
                                    <td width="5%">6</td>
                                    <td width="5%">1</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">176</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">176</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Chanda</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">10</td>
                                    <td width="5%">62</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">74</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">74</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Ganeshpur</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">36</td>
                                    <td width="5%">27</td>
                                    <td width="5%">192</td>
                                    <td width="5%">46</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">303</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">303</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Landasangvi</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">2</td>
                                    <td width="5%">52</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">54</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">54</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Nishanghat</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Arli (Buzurg)</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">11</td>
                                    <td width="10%" style="background-color: #c5dda2">11</td>
                                    <td width="5%">14</td>
                                    <td width="5%">5</td>
                                    <td width="5%">138</td>
                                    <td width="5%">20</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">177</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">188</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Takli</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Kumbhajheri</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Ramai</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Jamuldhari</td>
                                    <td width="10%">0</td>
                                    <td width="5%">9</td>
                                    <td width="5%">1</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">10</td>
                                    <td width="5%">4</td>
                                    <td width="5%">5</td>
                                    <td width="5%">60</td>
                                    <td width="5%">6</td>
                                    <td width="5%">1</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">76</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">86</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Yapalguda</td>
                                    <td width="10%">0</td>
                                    <td width="5%">3</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">3</td>
                                    <td width="5%">58</td>
                                    <td width="5%">16</td>
                                    <td width="5%">100</td>
                                    <td width="5%">110</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">284</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">287</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Anukunta</td>
                                    <td width="10%">0</td>
                                    <td width="5%">14</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">14</td>
                                    <td width="5%">112</td>
                                    <td width="5%">52</td>
                                    <td width="5%">162</td>
                                    <td width="5%">124</td>
                                    <td width="5%">56</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">506</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">520</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Battisawargaon</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">116</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">116</td>
                                    <td width="5%">36</td>
                                    <td width="5%">27</td>
                                    <td width="5%">92</td>
                                    <td width="5%">46</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">203</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">319</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Mavala</td>
                                    <td width="10%">0</td>
                                    <td width="5%">27</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">27</td>
                                    <td width="5%">184</td>
                                    <td width="5%">112</td>
                                    <td width="5%">576</td>
                                    <td width="5%">4</td>
                                    <td width="5%">45</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">921</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">948</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Kachkanti</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">38</td>
                                    <td width="5%">13</td>
                                    <td width="5%">124</td>
                                    <td width="5%">36</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">211</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">211</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Tontoli</td>
                                    <td width="10%">0</td>
                                    <td width="5%">9</td>
                                    <td width="5%">1</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">10</td>
                                    <td width="5%">66</td>
                                    <td width="5%">34</td>
                                    <td width="5%">200</td>
                                    <td width="5%">60</td>
                                    <td width="5%">18</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">378</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">388</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Kottur (Nevegaon)</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Borenur</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Lokari</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">10</td>
                                    <td width="5%">3</td>
                                    <td width="5%">36</td>
                                    <td width="5%">22</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">71</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">71</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Ankoli</td>
                                    <td width="10%">0</td>
                                    <td width="5%">2</td>
                                    <td width="5%">1</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">3</td>
                                    <td width="5%">70</td>
                                    <td width="5%">23</td>
                                    <td width="5%">208</td>
                                    <td width="5%">72</td>
                                    <td width="5%">20</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">393</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">396</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Waghapur</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">12</td>
                                    <td width="5%">6</td>
                                    <td width="5%">26</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">44</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">44</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Maleborgaon</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">12</td>
                                    <td width="5%">6</td>
                                    <td width="5%">26</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">44</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">44</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Chinchughat</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Ankapoor</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Asodabhurki</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Pippaldhari</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">10</td>
                                    <td width="5%">0</td>
                                    <td width="5%">10</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">22</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">22</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Wanwat</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">10</td>
                                    <td width="5%">2</td>
                                    <td width="5%">10</td>
                                    <td width="5%">16</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">38</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">38</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Belluri</td>
                                    <td width="10%">0</td>
                                    <td width="5%">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">2</td>
                                    <td width="5%">0</td>
                                    <td width="5%">5</td>
                                    <td width="5%">24</td>
                                    <td width="5%">6</td>
                                    <td width="5%">1</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">36</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">38</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Khandala</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Lohara</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Hathigutta</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Tippa</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Maregaon</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Khanapoor</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Chichadhari</td>
                                    <td width="10%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">0</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">0</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr><tr>
		<td>
                            <table style="text-align: left; width: 100%;">
                                <tbody><tr>
                                   <td width="10%">Tahsil-Adilabad<br>Village-Dasnapur (CT)</td>
                                    <td width="10%">0</td>
                                    <td width="5%">14</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">14</td>
                                    <td width="5%">62</td>
                                    <td width="5%">86</td>
                                    <td width="5%">352</td>
                                    <td width="5%">10</td>
                                    <td width="5%">13</td>
                                    <td width="5%">0</td>
                                    <td width="10%" style="background-color: #c5dda2">523</td>
                                    <td width="10%" style="background-color: #3A5218; color: #FFFFCC;">537</td>

                                </tr>
                            </tbody></table>
                        </td>
	</tr>
</tbody></table>

                    

                    

                    
                    

                    
                    <div class="clear">
                    </div>
                </div>
                <div class="bottom">
                </div>
                <div class="clear">
                </div>
            </div>
        </div>
        <div class="clear">
        </div>
        <div id="footer">
            <div id="footerlinks">
                <ul class="footermargin">
                    <li><a href="FarmerHome.aspx" title="Home Page">Home</a></li>
                    <li><a href="aboutus.html" title="About Us">About Us</a></li>
                    <li><a href="help.html" title="Help">Help</a></li>
                    <li><a href="http://agricoop.nic.in/weather.html" title="Weather Forecast" target="_blank">Weather Forecast</a></li>
                    <!--<li><a href="#" title="Queries">Queries </a></li>-->
                    <li><a href="feedback/Default.aspx" title="Feedback">Feedback </a></li>
                    <li><a href="http://agricoop.nic.in/ecitizen.html" title="RTI" target="_self">RTI</a></li>
                    <li><a href="sitemap.html" title="Sitemap">Sitemap</a></li>
                    <li><a href="accessibility.html" title="Accessibility Statement">Accessibility Statement</a></li>
                    <li class="last"><a href="websitepolicy.html" title="Website Policy">Website Policy
                    </a></li>
                </ul>
            </div>
            <div id="owner">
                This website belongs to Department of Agriculture &amp; Cooperation,<br>
                Ministry of Agriculture, Government of India
            </div>
        </div>
    </form>


</body></html>'''

from bs4 import BeautifulSoup
soup = BeautifulSoup(html)
## refers to the html part where data is stored
tag_table = soup.find_all("table", style="text-align: left; width: 100%;" )

#tag_table[0]
import pandas as pd
from pandas import DataFrame, Series
data_all=pd.DataFrame()
for i in range(0,len(tag_table)):
    data_text = tag_table[i].text #extract text from the tag 
    data_replace = data_text.replace('\n', ',').replace(',,','').replace(' ','')
    data_string = data_replace.encode() #convert unicode into string
    data_list = data_string.split() # convert string into list
    df = pd.DataFrame(data_list) #convert into dataframe
    data_all =data_all.append(df) # append all iterations into final dataframe
    #print data_all
data_all.to_csv('C:\\Users\\malaniaayushi\\Desktop\\data1.csv', index = False, sep='\t') # write
      

    
