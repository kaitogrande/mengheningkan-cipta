  <title>FaSHion : What's Your Style!</title>

   <script type="text/javascript" src="https://cdn.jsdelivr.net/npm/brython@3.10/brython.min.js"></script>
  <script type="text/python" src="main.py"></script>
    <style>
        body{
            font-family: Arial, sans-serif;
            max-width:800px;
            margin:auto;
            padding:20px;
        }

        button{
            display:block;
            width:100%;
            margin:10px 0;
            padding:12px;
            cursor:pointer;
        }

        .hasil{
            background:#f4f4f4;
            padding:15px;
            border-radius:10px;
        }
    </style>
</head>

<body onload="brython()">

<h1>FaSHion : Show Your Fits!</h1>
<p>Cari tahu fashion style tersembunyimu</p>

<div id="quiz"></div>

<script type="text/python">
