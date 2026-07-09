document.addEventListener(
    "DOMContentLoaded",
    () => {

        const tableBody =
            document.getElementById(
                "medicine-body"
            );

        const addButton =
            document.getElementById(
                "add-medicine"
            );

        if (
            !tableBody ||
            !addButton
        ) {
            return;
        }

        function updateIndexes() {

            const rows =
                tableBody.querySelectorAll(
                    ".medicine-row"
                );

            rows.forEach(
                (
                    row,
                    index,
                ) => {

                    row.querySelector(
                        '[name="morning"]'
                    ).value = index;

                    row.querySelector(
                        '[name="afternoon"]'
                    ).value = index;

                    row.querySelector(
                        '[name="night"]'
                    ).value = index;

                }
            );

        }

        addButton.addEventListener(
            "click",
            () => {

                const firstRow =
                    tableBody.querySelector(
                        ".medicine-row"
                    );

                const newRow =
                    firstRow.cloneNode(
                        true
                    );

                newRow
                    .querySelectorAll(
                        "input"
                    )
                    .forEach(
                        (
                            input,
                        ) => {

                            switch (
                                input.type
                            ) {

                                case "checkbox":

                                    input.checked = false;
                                    break;

                                case "number":

                                    input.value = 1;
                                    break;

                                default:

                                    input.value = "";

                            }

                        }
                    );

                newRow
                    .querySelector(
                        "select"
                    )
                    .selectedIndex = 0;

                tableBody.appendChild(
                    newRow
                );

                updateIndexes();

                if (
                    typeof lucide !==
                    "undefined"
                ) {
                    lucide.createIcons();
                }

            }
        );


        tableBody.addEventListener(
            "click",
            (event) => {

                const button =
                    event.target.closest(
                        ".remove-medicine"
                    );

                if (!button) {
                    return;
                }

                const rows =
                    tableBody.querySelectorAll(
                        ".medicine-row"
                    );

                if (rows.length === 1) {

                    alert(
                        "At least one medicine is required."
                    );

                    return;
                }

                button
                    .closest(
                        ".medicine-row"
                    )
                    .remove();

                updateIndexes();

            }
        );

        updateIndexes();

    }
);
