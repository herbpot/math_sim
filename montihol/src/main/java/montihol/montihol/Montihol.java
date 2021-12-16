package montihol.montihol;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;

public final class Montihol extends JavaPlugin {

    @Override
    public void onEnable() {
        getLogger().info("-----------------------------");
        getLogger().info("the montihol plugin is online");
        getLogger().info("-----------------------------");
        // Plugin startup logic
        Bukkit.getPluginManager().registerEvents(new Event(), this);

    }

    @Override
    public void onDisable() {
        // Plugin shutdown logic
    }
}
