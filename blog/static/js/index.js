// 非同期でいいね機能を実装

// API呼び出しが完了したときに呼ばれるコールバック関数
// HTML中の'like1', 'like2'...といったIDを持つ要素の内容をレスポンス中のlikeの値で置き換える
function callback(json) {
    var element = document.getElementById('like' + json.id);
    element.textContent = json.like;
}

// 関数が呼ばれたときに、今回作成したAPIを呼び出す
function like(article_id) {
    var req = new XMLHttpRequest();
    req.onreadystatechange = function() {
        // XMLHttpRequest.readyState = 4：DONE
        // XMLHttpRequest.status = 200：DONE
        if ((req.readyState == 4) && (req.status == 200)) {
            var json = JSON.parse(req.responseText);
            callback(json);
        }
    }
    req.open('GET', '/api/articles/' + article_id + '/like');
    req.send(null);
}