
function addResourceField() {
    const resourceFields = document.getElementById('resource-fields');
    const resourceField = document.createElement('div');
    resourceField.className = 'resource-field';
    resourceField.innerHTML = `
                <div class="form-row">
                    <div class="form-group col-md-6">
                        <input type="text" name="resource_name" class="form-control" placeholder="Resource Name" required>
                    </div>
                    <div class="form-group col-md-4">
                        <input type="number" name="resource_amount" class="form-control" placeholder="Amount" required>
                    </div>
                    <div class="form-group col-md-2">
                        <button type="button" class="btn btn-danger" onclick="removeResourceField(this)">Remove</button>
                    </div>
                </div>
            `;
    resourceFields.appendChild(resourceField);
}

function removeResourceField(button) {
    const resourceFields = document.getElementById('resource-fields');
    const resourceField = button.parentNode.parentNode.parentNode;
    resourceFields.removeChild(resourceField);
}
function sendFormData(){
    document.getElementById('createQuestForm').addEventListener('submit', function (event) {
        event.preventDefault();
        const formData = new FormData(document.getElementById('createQuestForm'));
        const resources = [];

        // Collect resource data
        document.querySelectorAll('.resource-field').forEach(function (field) {
            const resourceName = field.querySelector('input[name="resource_name"]').value;
            const resourceAmount = field.querySelector('input[name="resource_amount"]').value;
            resources.push({ name: resourceName, amount: resourceAmount });
        });

        formData.append('resources', JSON.stringify(resources));

        // Send the POST request
        fetch('/quests/create', {
            method: 'POST',
            body: formData
        })
            .then(response => response.json())
            .then(data => {
                // Handle the response here (e.g., show a success message)
                console.log(data);
            })
            .catch(error => {
                // Handle errors here
                console.error(error);
            });
    });
}


function edit_quest(quest){
    $('#')
}

function delete_quest(quest){

}

