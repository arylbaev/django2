


async function makeRequest(url, method, body){
  let headers = {
      'X-Requested-With': 'XMLHttpRequest',
      'Content-Type': 'application/json'
    }

  if (method == 'post'){
    const csrf = document.querySelector('[name = csrfmiddlewaretoken]').value
    headers['X-CSRFToken'] = csrf
  }

  let response = await fetch(url, {
    method: method,
    headers: headers,
    body: body
  })

  return await response.json()
}

async function send_comment(){
  console.log('comment')
  const formElement = document.getElementById('comment_form');
  formElement.addEventListener('submit', (e) => {
    e.preventDefault();
    const formData = new FormData(formElement);
    const comment = formData.get('comment');
    url =
    makeRequest(url, method='post', body=JSON.stringify({user_id: user_id, post_id: post_id}))
});

}