async function loadUsers() {

    const container = document.getElementById("users");
    container.innerHTML = "<h2>Loading...</h2>";

    try {

        const response = await fetch(
            "https://randomuser.me/api/?results=6"
        );

        const data = await response.json();

        container.innerHTML = "";

        data.results.forEach(user => {

            container.innerHTML += `
                <div class="card">
                    <img src="${user.picture.large}">
                    <h3>${user.name.first} ${user.name.last}</h3>
                    <p>${user.email}</p>
                    <p>${user.location.country}</p>
                </div>
            `;
        });

    } catch(error) {
        container.innerHTML = "<h2>Error Loading Data</h2>";
        console.log(error);
    }
}