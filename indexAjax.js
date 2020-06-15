
    var ws = new WebSocket("ws://127.0.0.1:1236/");
    ws.onmessage = function (event) {
        var 
            content = document.createTextNode(event.data),
            dt = document.getElementById('dt'),
            temp = document.getElementById('temp');
            test = document.getElementById('test');
            image = document.getElementById('img');
        
        if (content.substringData(0, 2) == '0 ')
        {
            dt.innerHTML = "";
            dt.append(content.substringData(2, content.length - 2));
        }
        else if (content.substringData(0, 2) == '1 ')
        {
            temp.innerHTML = "";
            temp.append(content.substringData(2, content.length - 2));
        }
        else if (content.substringData(0, 2) == '2 ')
        {
            test.innerHTML = "";
            test.append(content.substringData(2, content.length - 2));
        }
        else if (content.substringData(0, 2) == '9 ')
        {
            var decodeTest = decode(content.substringData(2, content.length - 2))
            image.src=""; 
            image.src = "data:image/jpg;base64, " + decodeTest;
        }
    };

    function decode(s)
    {
        const unicodeString = s.replace(
            /[\u00e0-\u00ef][\u0080-\u00bf][\u0080-\u00bf]/g,
            function(c) {
                var cc = ((c.charCodeAt(0)&0x0f)<<12) | ((c.charCodeAt(1)&0x3f)<<6) | (c.charCodeAt(2)&0x3f);
                return String.fromCharCode(cc);
            }).replace(
                /[\u00c0-\u00df][\u0080-\u00bf]/g,
                function(c) {
                    var cc = (c.charCodeAt(0)&0x1f)<<6 | c.charCodeAt(1)&0x3f;
                    return String.fromCharCode(cc);
                }
            );
        return unicodeString;
    }